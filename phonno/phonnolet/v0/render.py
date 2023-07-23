def transform_to_style_attr(style_object):
    style = ""
    for key, value in style_object.items():
        style += "{}:{};".format(key, value)
    return style.strip()


def get_anno_style(type):
    if type == "query":
        return transform_to_style_attr(
            {
                "display": "inline-block",
                "max-width": "200px",
                "max-height": "64px",
                "min-height": "20px",
                "margin": "3px 0",
                "vertical-align": "bottom",
                "border-color": "rgba(143, 173, 249, 0.2)",
                "padding-bottom": "3px",
                "border-style": "none none solid;",
                "border-width": "1.5px",
            }
        )
    return ""


def show_annotations(args, style="query"):
    img_style = get_anno_style(style)
    print(args, img_style)


# print(transform_to_style_attr({"a": 1, "b": 2}))
show_annotations([], "query")
