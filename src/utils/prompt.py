# from enum import Enum

EXAMPLE_JSON_PATH = "example.json"

with open(EXAMPLE_JSON_PATH, "r", encoding="utf-8") as f:
    example_json_text = f.read()
# class PromptList(Enum):


# EMAIL_TEMPLATE_PROMPT = """You must generate a fully dynamic email template in the EXACT STRUCTURE below.
# You MUST allow multiple columns per row.

# You have to chouse layouts per row from below:

# Layouts:

# (1) 2 colomn layout
# - column/2-50-image-text-button (Means both columns have image, text and button)
# - column/1-50-image/1-50-text-button (Means first column has image, second column has text and button)
# - column/1-50-text-button/1-50-image (Means first column has text and button, second column has image)
# - column/1-50-image/1-50-text   (Means first column has image, second column has text)
# - column/1-50-text/1-50-image (Means first column has text, second column has image)
# - column/2-50-image (Means both columns have image)
# - column/2-50-button (Means both columns have button)

# (2) 3 Column layout
# - column/3-33-image-text-button (Means all three columns have image, text and button)
# - column/3-33-image-text (Means all three columns have image and text)
# - column/3-33-image (Means all three columns have image)
# - column/1-33-image/2-33-text (First column has image, second and third columns have text)
# - column/2-33-text/1-33-image (First and second columns have text, third column has image)
# - column/3-33-text (Means all three columns have text)
# - column/3-33-button  (Means all three columns have button)

# (3) 4 column layout:
# - column/4-25-image-text-button (Means all four columns have image, text and button)
# - column/4-25-image-text (Means all four columns have image and text) 
# - column/4-25-image (Means all four columns have image)
# - column/1-25-image/1-25-text/1-25-image/1-25-text (Means first column has image, second column has text, third column has image, fourth column has text)
# - column/1-25-text/1-25-image/1-25-text/1-25-image (Means first column has text, second column has image, third column has text, fourth column has image)
# - column/1-25-image/3-25-text (Means first column has image, rest three columns have text)
# - column/4-25-text (Means all four columns have text)
# - column/4-25-button (Means all four columns have button)

# ====================================================
# 📌 REQUIRED OUTPUT STRUCTURE (UPDATED — MULTI-COLUMN)
# ====================================================

# {
#   "field_list": [
#     {
#       "id": "<unique>",
#       "rowConfig": {"columnLayoutCategory" : <Chose from above layouts for multi column layout> },
#       "fieldDetail": [
#         {
#           "id": "<unique>",
#           "colConfig": {},
#           "fieldArray": [
#             {
#               "id": "<unique>",
#               "icon": "<icon>",
#               "label": "<Text | Image | Button | Divider>",
#               "name": "<text | image | button | divider>",
#               "type": "<text | image | button | divider>",
#               "fieldValue": {
#                 "text": {
#                   "id": "<unique>",
#                   "subType": "text",
#                   "text": "<html or plain text>",
#                   "Configuration": {}
#                 }
#                 OR
#                 "img": {
#                   "id": "<unique>",
#                   "subType": "image",
#                   "url": "<image URL>",
#                   "Configuration": {}
#                 }
#                 OR
#                 "button": {
#                   "id": "<unique>",
#                   "subType": "button",
#                   "text": "<button text>",
#                   "buttonLink": "<URL>",
#                   "Configuration": {}
#                 }
#                 OR
#                 "divider": {
#                   "id": "<unique>",
#                   "subType": "divider",
#                   "Configuration": {}
#                 }
#               }
#             }
#             , // The model MAY add more columns here
#           ]
#         }
        
#       ]
#     }
#     , // The model MAY add more rows here
#   ]
# }

# ====================================================
# 📌 RULES THE MODEL MUST FOLLOW
# ====================================================

# 1. The structure above is STRICT and MUST be followed.
# 2. Every row MUST have **1 or more columns**.
# 3. Every column MUST have **1 or more fields**.
# 4. Multiple columns MUST be allowed inside fieldDetail.
# 5. The model must dynamically decide:
#    - number of rows
#    - number of columns per row (1, 2, 3, etc.)
#    - field order and content
# 6. Use only correct fieldValue keys:
#    - text → text
#    - image → img
#    - button → button
#    - divider → divider
# 7. Use Unsplash URLs if user does not give images.
# 8. For multi-column layouts: column widths MUST sum to 100%.
# 9. In id field you have to put 8 character unique string including numerical and small alphabets.
# 10. All IDs (row, column, field, content) MUST be unique strings.

# ====================================================
# 📌 DO NOT:
# ====================================================
# - Change structure names
# - Remove required keys
# - Put markdown or comments in output
# - Collapse fieldDetail into one column only

# ====================================================
# END OF RULES
# ====================================================
# """


# EMAIL_TEMPLATE_PROMPT = """


# You must generate a fully dynamic email template in the EXACT STRUCTURE below.
# You MUST allow multiple columns per row.

# ====================================================
# 📌 LAYOUTS — YOU MUST CHOOSE ONLY FROM THESE
# ====================================================

# (1) 2 colomn layout
# - column/2-50-image-text-button (Means both columns have image, text and button)
# - column/1-50-image/1-50-text-button (Means first column has image, second column has text and button)
# - column/1-50-text-button/1-50-image (Means first column has text and button, second column has image)
# - column/1-50-image/1-50-text   (Means first column has image, second column has text)
# - column/1-50-text/1-50-image (Means first column has text, second column has image)
# - column/2-50-image (Means both columns have image)
# - column/2-50-button (Means both columns have button)

# (2) 3 Column layout
# - column/3-33-image-text-button (Means all three columns have image, text and button)
# - column/3-33-image-text (Means all three columns have image and text)
# - column/3-33-image (Means all three columns have image)
# - column/1-33-image/2-33-text (First column has image, second and third columns have text)
# - column/2-33-text/1-33-image (First and second columns have text, third column has image)
# - column/3-33-text (Means all three columns have text)
# - column/3-33-button  (Means all three columns have button)

# (3) 4 column layout:
# - column/4-25-image-text-button (Means all four columns have image, text and button)
# - column/4-25-image-text (Means all four columns have image and text) 
# - column/4-25-image (Means all four columns have image)
# - column/1-25-image/1-25-text/1-25-image/1-25-text (Means first column has image, second column has text, third column has image, fourth column has text)
# - column/1-25-text/1-25-image/1-25-text/1-25-image (Means first column has text, second column has image, third column has text, fourth column has image)
# - column/1-25-image/3-25-text (Means first column has image, rest three columns have text)
# - column/4-25-text (Means all four columns have text)
# - column/4-25-button (Means all four columns have button)

# ====================================================
# 📌 IMPORTANT LAYOUT RULE (FIXED)
# ====================================================

# - If a row has **more than one column**, you MUST include:
  
#   "rowConfig": { "columnLayoutCategory": "<one layout from above>" }

# - If a row has **only one column**, you MUST use:
  
#   "rowConfig": {}

#   (Do NOT include columnLayoutCategory for single-column rows.)

# ====================================================
# 📌 REQUIRED OUTPUT STRUCTURE (CRITICAL)
# ====================================================

# {
#   "field_list": [
#     {
#       "id": "<8-char unique>",
#       "rowConfig": { 
#           "columnLayoutCategory": "<ONLY for multi-column rows>" 
#       },
#       "fieldDetail": [
#         {
#           "id": "<8-char unique>",
#           "colConfig": {},
#           "fieldArray": [
#             {
#               "id": "<8-char unique>",
#               "icon": "<icon>",
#               "label": "<Text | Image | Button | Divider>",
#               "name": "<text | image | button | divider>",
#               "type": "<text | image | button | divider>",

#               "fieldValue": {
#                 "text": {
#                   "id": "<8-char unique>",
#                   "subType": "text",
#                   "text": "<html or plain text>",
#                   "Configuration": {}
#                 }
#                 OR
#                 "img": {
#                   "id": "<8-char unique>",
#                   "subType": "image",
#                   "url": "<image URL>",
#                   "Configuration": {}
#                 }
#                 OR
#                 "button": {
#                   "id": "<8-char unique>",
#                   "subType": "button",
#                   "text": "<button text>",
#                   "buttonLink": "<URL>",
#                   "Configuration": {}
#                 }
#                 OR
#                 "divider": {
#                   "id": "<8-char unique>",
#                   "subType": "divider",
#                   "Configuration": {}
#                 }
#               }
#             }
#             // The model MAY add more fields in this column
#           ]
#         }
#         // The model MAY add more columns inside fieldDetail
#       ]
#     }
#     // The model MAY add more rows
#   ]
# }

# ====================================================
# 📌 STRICT RULES THE MODEL MUST FOLLOW
# ====================================================

# 1. Every row MUST have **1 or more columns**.
# 2. Every column MUST have **1 or more fields**.
# 3. When a row has 2/3/4 columns, you MUST select a layout from the list.
# 4. When a row has 1 column, DO NOT include columnLayoutCategory.
# 5. Every “fieldArray” item MUST contain:
#    - id  
#    - icon  
#    - label  
#    - name  
#    - type  
#    - fieldValue  
# 6. The correct fieldValue key MUST be EXACT:
#    - text    → "text"
#    - image   → "img"
#    - button  → "button"
#    - divider → "divider"
# 7. fieldValue object MUST contain:
#    - id  
#    - subType (text/image/button/divider)
#    - Configuration: {} (empty)
# 8. For multi-column rows: column widths MUST total 100%.
# 9. Use Unsplash URLs if user does not provide image URLs.
# 10. All IDs for rows, columns, fields, and content MUST be:
#     - EXACTLY 8 characters  
#     - lowercase alphabets + numbers only  
#     - unique across the structure  

# ====================================================
# 📌 YOU MUST DYNAMICALLY DECIDE
# ====================================================

# - Number of rows  
# - Number of columns per row (1/2/3/4)  
# - Correct layout for multi-column rows  
# - Field order (image → text → content → button etc.)  
# - All text content  
# - All image URLs  
# - All button texts and URLs  

# ====================================================
# 📌 YOU MUST NOT
# ====================================================

# - Use any layout not listed above  
# - Add unknown keys  
# - Change required key names  
# - Add markdown or explanation  
# - Collapse everything into one column  
# - Use “fieldValue”: { "image": … } — MUST be "img"  

# ====================================================
# END OF RULES
# ====================================================

# """

EMAIL_TEMPLATE_PROMPT = f"""
You are an Email Template Generator. Return ONLY a single JSON object that uses the exact structure below. Do NOT add, remove, rename, or simplify keys. No markdown, no explanation, only JSON.

I have share below example understand it structure deeply do not copy from it use it as refrence 
{example_json_text}

REQUIRED OUTPUT STRUCTURE (STRICT)

{{
  "field_list": [
    {{
      "id": "<8char_alnum>",
      "rowConfig": {{  
         // ONLY include "columnLayoutCategory" when this row has more than 1 column
         // e.g. "columnLayoutCategory": "column/2-50-image-text-button"
      }},
      "fieldDetail": [
        {{
          "id": "<8char_alnum>",
          "colConfig": {{   
             // for multi-column rows include "width": <int 1-100>
          }},
          "fieldArray": [
            {{
              "id": "<8char_alnum>",
              "icon": "<icon>",
              "label": "<Text | Image | Button | Divider>",
              "name": "<text | image | button | divider>",
              "type": "<text | image | button | divider>",
              "fieldValue": {{
                // For text fields:
                "text": {{
                  "id": "<8char_alnum>",
                  "subType": "text",
                  "text": "<html or plain text>",
                  "Configuration": {{}}
                }}
                // OR for image fields:
                OR
                "img": {{
                  "id": "<8char_alnum>",
                  "subType": "image",
                  "url": "<image URL (Unsplash if none provided)>",
                  "Configuration": {{}}
                }}
                // OR for button fields:
                OR
                "button": {{
                  "id": "<8char_alnum>",
                  "subType": "button",
                  "text": "<button text>",
                  "buttonLink": "<URL>",
                  "Configuration": {{}}
                }}
                // OR for divider fields:
                OR
                "divider": {{
                  "id": "<8char_alnum>",
                  "subType": "divider",
                  "Configuration": {{}}
                }}
              }}
            }}
            // model MAY add more field items in this column
          ]
        }}
        // model MAY add more column objects for multi-column rows
      ]
    }}
    // model MAY add more row objects
  ]
}}

LAYOUTS (allowed — model MUST pick per multi-column row from exactly these strings)

2-column choices:
- column/2-50-image-text-button
- column/1-50-image/1-50-text-button
- column/1-50-text-button/1-50-image
- column/1-50-image/1-50-text
- column/1-50-text/1-50-image
- column/2-50-image
- column/2-50-button
- column/2-50-text

3-column choices:
- column/3-33-image-text-button
- column/3-33-image-text
- column/3-33-image
- column/1-33-image/2-33-text
- column/2-33-text/1-33-image
- column/3-33-text
- column/3-33-button

4-column choices:
- column/4-25-image-text-button
- column/4-25-image-text
- column/4-25-image
- column/1-25-image/1-25-text/1-25-image/1-25-text
- column/1-25-text/1-25-image/1-25-text/1-25-image
- column/1-25-image/3-25-text
- column/4-25-text
- column/4-25-button

MANDATORY RULES (model must obey)
1. Output must be valid JSON only — nothing else.
2. Every row must have 1 or more columns. Every column must have 1 or more fields.
3. If a row has more than one column, the rowConfig MUST include:
     "columnLayoutCategory": "<one allowed layout string>"
   If a row has exactly one column, rowConfig MUST NOT include "columnLayoutCategory".
4. For multi-column rows, colConfig MUST include numeric widths that sum to exactly 100.
5. Do not invent layout strings — only use the allowed ones above.
6. IDs must be exactly 8 characters, lowercase alphanumeric (a-z, 0-9).
7. Every field entry must include id, icon, label, name, type, fieldValue.
8. The fieldValue key must match the type exactly: text → text, image → img, etc.
9. Use Unsplash images when user does not provide images.
10. Do NOT change any key names or nesting.
11. Do not include any HTML, markdown, in text fields — only plain text.
12. Do not include any px, %, or units in width , hight ,pargin , padding , etc. values — only integers.
13. When outputting JSON, use real emojis instead of escaped Unicode sequences.
14. use this url "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" for images


DYNAMIC DECISIONS (model should decide)
- number of rows
- number of columns per row (1-4)
- which allowed layout to use for multi-column rows
- appropriate ordering of fields (image, text, divider, button, etc.)
- generating content with correct tone and purpose

END
"""
# iPhFjyw5 
