from jsonschema import validate

schema_2020_12 = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "post_id": {
          "type": "integer"
        },
        "category": {
          "type": "string"
        },
        "date_posted": {
          "type": "string"
        },
        "article": {
          "type": "object",
          "properties": {
            "article_title": {
              "type": "string"
            },
            "full_article": {
              "type": "string"
            },
            "username": {
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
            "article_title",
            "full_article",
            "username",
            "summary_title",
            "summary"
          ]
        }
      },
      "required": [
        "post_id",
        "category",
        "date_posted",
        "article"
      ]
    }
  ]
}

validate(
    instance={
      "post_id": 1,
      "category": "wealth",
      "date_posted": "05/11/2023",
      "article": {
        "article_title": "pariatur quis sit et ex",
        "full_article": "Enim consequat aliquip in amet fugiat. Fugiat exercitation proident culpa ullamco laboris",
        "username": "Alonzo Johnson",
        "summary_title": "deserunt cupidatat",
        "summary": "Dolore qui fugiat excepteur excepteur tempor in sunt irure",
      },
    },
    schema=schema_2020_12,
)
# Given JSON data is Valid
