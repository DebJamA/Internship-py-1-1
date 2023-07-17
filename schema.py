from jsonschema import validate

schema = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$ref": "#/definitions/posts",
    "definitions": {
        "posts": {
            "type": "object",
            "properties": {
                "blog": {
                    "type": "object",
                    "additionalProperties": {
                        "$ref": "#/definitions/Blog"
                    }
                }
            },
            "required": [
                "blog"
            ],
            "title": "posts"
        },
        "Blog": {
            "type": "object",
            "properties": {
                "post_id": {
                    "type": "integer"
                },
                "analyst": {
                    "type": "string"
                },
                "category": {
                    "type": "string"
                },
                "date_posted": {
                    "type": "string",
                    "format": "date"
                },
                "article_title": {
                    "type": "string"
                },
                "article": {
                    "type": "string"
                },
                "summary_title": {
                    "type": "string"
                },
                "summary": {
                    "type": "string"
                }
            },
            "required": [
                "analyst",
                "article",
                "article_title",
                "category",
                "date_posted",
                "post_id",
                "summary",
                "summary_title"
            ],
            "title": "Blog"
        }
    }
}

validate(
    instance={
        "blog": {
            "post0": {
                "post_id": 0,
                "analyst": "Alberta Jast",
                "category": "Wealth",
                "date_posted": "2023-06-11",
                "article_title": "BigBiz CEO Net Worth Increases",
                "article": "BigBiz CEO velit adipisicing laborum laborum tempor duis...",
                "summary_title": "BigBiz Stock Will Rise Too",
                "summary": "BigBiz stock culpa est adipisicing..."
            },
        },
    },
    schema=schema,
)
print("Given JSON data is Valid")
