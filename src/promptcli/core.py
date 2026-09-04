def render(template: str, values: dict[str, object]) -> str:
    """Render simple {name} placeholders using supplied values."""
    return template.format_map(values)
