INDEX_TEXT_BASIC_EMOJI = 39
CATEGORIES = ["Basic_Emoji", "Emoji_Keycap_Sequence", "RGI_Emoji_Flag_Sequence", "RGI_Emoji_Tag_Sequence",
              "RGI_Emoji_Modifier_Sequence"]
SPACE = "231A..231B    ; Basic_Emoji                  "
INDEX_OF_OPEN_BRACKET = 123
INDEX_OF_FIRST_HASHTAG = 110
INDEX_OF_FIRST_SEP = 14
INDEX_OF_SECOND_SEP = 45


def get_hex_code(line):
    return str(line[:INDEX_OF_FIRST_SEP - 1]).strip()


def get_description(line):
    return str(line[INDEX_OF_SECOND_SEP + 1:INDEX_OF_FIRST_HASHTAG - 1]).strip()


def get_category(line):
    return str(line[INDEX_OF_FIRST_SEP + 1:INDEX_OF_SECOND_SEP - 1]).strip()


def get_emoji(line):
    return str(line[INDEX_OF_OPEN_BRACKET + 1:]).replace(")", "").strip()


if __name__ == "__main__":
    path = "emoji-sequences.txt" # **TODO**
    output = "OutputPath.kt"  # **TODO**
    f = open(path, "r", encoding="UTF-8")
    content = f.readlines()[INDEX_TEXT_BASIC_EMOJI:]
    f.close()
    with open(output, "w+", encoding="UTF-8") as f:
        f.write("val emojiData = listOf(")
        print(content[1])
        emojis = 0
        unknown_cat_count = 0
        for line in content:
            # if line.startswith("# E"):
            #    print("HEAD>> "+line)
            # if line != "":
            #     f=line.find(")")
            #     print(f)
            #     print(line)
            emoji = get_emoji(line)
            if emoji != "":
                emojis += 1
                print("---")
                hex_code = get_hex_code(line)
                print("Hex : " + hex_code)
                is_range = emoji.__contains__("..")
                str_is_range = "false"
                if is_range:
                    str_is_range = "true"
                    print("Emoji : " + emoji[0])
                    print("Emoji : " + emoji[3])
                else:
                    print("Emoji : " + emoji)
                cat = get_category(line)
                if cat != "":
                    print("Category : " + cat)
                desc = get_description(line)
                if desc != "":
                    print("Description : " + desc)
                if cat in CATEGORIES:
                    category = CATEGORIES.index(cat)
                    print(f"CategoryId={category}")
                    f.write(
                        f"EmojiItem(hexCode=\"{hex_code}\",emojiContent=\"{emoji}\",category={category},description=\"{desc}\",isRange={str_is_range}), ")
                else:
                    unknown_cat_count += 1
                    print("CategoryId=Unknown!!!")

        print(f"Found {emojis} emojis, Unknown categories : {unknown_cat_count}")
        f.write(")")
        f.close()
        print(f"All data saved to {output}")

