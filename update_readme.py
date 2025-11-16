import yaml
import json

def resolve_ref(spec, ref):
	"""Разрешает ссылки в формате $ref"""
	if not ref.startswith('#'):
		return {}  # Внешние ссылки не поддерживаются
	parts = ref.split('/')[1:]
	current = spec
	for part in parts:
		current = current.get(part, {})
	return current


def parse_schema(spec, schema, indent=0):
	"""Рекурсивно парсит схему с поддержкой ссылок"""
	md = ""
	prefix = "  " * indent

	# Обработка ссылок
	if isinstance(schema, dict) and '$ref' in schema:
		schema = resolve_ref(spec, schema['$ref'])

	schema_type = schema.get("type", "object")

	if schema_type == "object":
		properties = schema.get("properties", {})
		required = schema.get("required", [])
		for prop, details in properties.items():
			# Обработка ссылок в свойствах
			if isinstance(details, dict) and '$ref' in details:
				details = resolve_ref(spec, details['$ref'])

			prop_type = details.get("type", "N/A")
			prop_desc = details.get("description", details.get("title", ""))
			req_mark = "**(required)**" if prop in required else ""
			if prop_desc:
				md += f"{prefix}- **{prop}** ({prop_type}) {req_mark}: {prop_desc}\n"
			else:
				prop_example = details.get("example", "N/A")
				md += f"{prefix}- **{prop}** ({prop_type}) {req_mark}: {prop_example}\n"

			# Рекурсивная обработка вложенных объектов
			if prop_type == "object":
				md += parse_schema(spec, details, indent + 1)
			elif prop_type == "array":
				items = details.get("items", {})
				md += f"{prefix}  - Array items:\n"
				md += parse_schema(spec, items, indent + 2)
	elif schema_type == "array":
		items = schema.get("items", {})
		md += f"{prefix}- Array of:\n"
		md += parse_schema(spec, items, indent + 1)
	else:
		md += f"{prefix}- Type: {schema_type}\n"

	return md


with open("api/openapi.yaml", "r") as f:
	spec = yaml.safe_load(f)

info = spec.get("info", {})
paths = spec.get("paths", {})

md = f"# 📘 API Documentation\n\n"
md += f"**Title:** {info.get('title', 'N/A')}\n\n"
md += f"**Version:** {info.get('version', 'N/A')}\n\n"
md += f"**Description:** {info.get('description', '')}\n\n"
md += f"**OpenApi File:** api/openapi.yaml\n\n"
md += f"---\n\n"

for path, methods in paths.items():
	for method, details in methods.items():
		summary = details.get("summary", "")
		description = details.get("description", "")
		parameters = details.get("parameters", [])
		request_body = details.get("requestBody", {})
		responses = details.get("responses", {})

		md += f"## `{method.upper()} {path}`\n\n"
		md += f"**Summary:** {summary}\n\n"
		if description:
			md += f"**Description:** {description}\n\n"

		# Обработка параметров с поддержкой ссылок
		if parameters:
			md += "**Parameters:**\n\n"
			md += "| Name | In | Type | Required | Description |\n"
			md += "|------|----|------|----------|-------------|\n"
			for p in parameters:
				# Обработка ссылок в параметрах
				if isinstance(p, dict) and '$ref' in p:
					p = resolve_ref(spec, p['$ref'])

				name = p.get("name", "")
				location = p.get("in", "")

				# Обработка ссылок в схеме параметра
				param_schema = p.get("schema", {})
				if isinstance(param_schema, dict) and '$ref' in param_schema:
					param_schema = resolve_ref(spec, param_schema['$ref'])

				ptype = param_schema.get("type", "")
				required = "Yes" if p.get("required", False) else "No"
				desc = p.get("description", "")
				md += f"| {name} | {location} | {ptype} | {required} | {desc} |\n"
			md += "\n"

		# Обработка тела запроса с поддержкой ссылок
		if request_body:
			# Разрешаем ссылки в requestBody
			if isinstance(request_body, dict) and '$ref' in request_body:
				request_body = resolve_ref(spec, request_body['$ref'])

			md += "**Request Body:**\n\n"
			content = request_body.get("content", {})
			for mime, c in content.items():
				md += f"Content-Type: `{mime}`\n\n"
				schema = c.get("schema", {})

				# Обработка ссылок в схеме
				if isinstance(schema, dict) and '$ref' in schema:
					schema = resolve_ref(spec, schema['$ref'])

				if schema:
					md += parse_schema(spec, schema)
					md += "\n"

				# Извлечение примера
				example = None
				if "example" in c:
					example = c["example"]
				elif "examples" in c and "default" in c["examples"]:
					example = c["examples"]["default"].get("value")

				if example:
					md += "**Example:**\n\n"
					md += "```json\n" + yaml.dump(example, sort_keys=False) + "```\n\n"

		# Обработка ответов
		if responses:
			md += "**Responses:**\n\n"
			for code, resp in responses.items():
				# Разрешаем ссылки в ответах
				if isinstance(resp, dict) and '$ref' in resp:
					resp = resolve_ref(spec, resp['$ref'])

				desc = resp.get("description", "")
				md += f"- **HTTP {code}**: {desc}\n"  # Добавляем HTTP-код

				content = resp.get("content", {})
				for mime, c in content.items():
					# Выводим Content-Type
					md += f"  - **Content-Type**: `{mime}`\n"

					# Обработка схемы ответа
					schema = c.get("schema", {})
					if schema:
						md += "  **Schema**:\n"
						md += parse_schema(spec, schema, indent=2)
						md += "\n"


					# Извлечение примера ответа
					example = None
					if "example" in c:
						example = c["example"]
					elif "examples" in c and "default" in c["examples"]:
						example = c["examples"]["default"].get("value")

					# Форматированный вывод примера
					if example:
						md += "  **Example**:\n"
						try:
							# Пытаемся красиво отформатировать JSON
							formatted_ex = json.dumps(example, indent=2, ensure_ascii=False)
							md += f"  ```json\n{formatted_ex}\n  ```\n"
						except:
							# Если не JSON - используем обычный вывод
							md += f"  ```\n{example}\n  ```\n"

		md += "\n---\n\n"

# Обновление README
with open("README.md", "r") as f:
	content = f.read()

start_tag = "<!-- DOCS_START -->"
end_tag = "<!-- DOCS_END -->"

before = content.split(start_tag)[0]
after = content.split(end_tag)[1]

new_readme = f"{before}{start_tag}\n{md}\n{end_tag}{after}"

with open("README.md", "w") as f:
	f.write(new_readme)