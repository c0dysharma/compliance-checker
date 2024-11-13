# Compliance Checker

This app will look for text in a url and compare it with the [standard](https://stripe.com/docs/treasury/marketing-treasury).

# Routes

> POST /compliance

## Request

```
{
	"url":"http://mercury.com/"
}
```

## Response

```
{
	"data": [
		{
			"non_compliant_issues": [
				{
					"policy_violation": String,
					"text": String,
          "error": String
				},
			]
		}
	],
	"success": Boolean
}
```

# ENV Requirements

Create a .env file and add these fields

```
GEMINI_API_KEY=KEY_HERE
```
