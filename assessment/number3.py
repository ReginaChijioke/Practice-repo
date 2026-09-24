def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"] = list(updated["tags"])
    updated["tags"].append(tag)
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")
print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])


ASSERTIONS 

"""
assert original["tags"] == ["python"]
assert changed["tags"] == ["python", "testing"]
changed["tags"].append("more")
assert original["tags"] == ["python"]
"""