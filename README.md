# EmojiDatasetReader
Converts emoji-dataset to kotlin list of `EmojiItem()`.
- Emoji dataset provided is of Unicode-14.0
- Latest dataset can be downloaded from https://unicode.org/Public/emoji/latest

## Credits for resources
- https://unicode.org
- https://emojipedia.org


### EmojiItem Syntax
[EmojiItem.kt](/EmojiItem.kt)
```kt
data class EmojiItem(
    val hexCode: String,
    val emojiContent: String,
    val category: Int,
    val description: String,
    val isRange: Boolean
)
```

Generated Sample
```kt
EmojiItem(
    hexCode = "1F60E",
    emojiContent = "😎",
    category = 0,
    description = "smiling face with sunglasses",
    isRange = false
)
```

## License
```

   Copyright 2023 Aditya Bavadekar

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```
