import IPython
from IPython.display import display, HTML


def transform_to_style_attr(style_object):
    style = ""
    for key, value in style_object.items():
        style += "{}:{};".format(key, value)
    return style.strip()


def get_anno_tet_style(type):
    if type == "query":
        return transform_to_style_attr(
            {
                "display": "inline-block",
                "margin": "3px 0",
            }
        )
    return ""


def get_anno_img_style(type):
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


def get_anno_container_style(type):
    if type == "query":
        return transform_to_style_attr(
            {
                "display": "flex",
                "gap": "4px",
                "align-items": "flex-end",
            }
        )
    return ""


def show_annotations(items, origin="", style="query"):
    root_style = get_anno_container_style(style)
    img_style = get_anno_img_style(style)
    txt_style = get_anno_tet_style(style)
    html_lines = []
    html_lines.append("<div data-name='annotations' style='{}'>".format(root_style))
    for item in items:
        if isinstance(item, list):
            [image_id, anno_id] = item
            url = "{}/{}#a{}".format(origin, image_id, int(anno_id) + 1)
            img_url = "{}/api/data/annotations_images?imageId={}&annoId={}".format(
                origin, image_id, str(anno_id)
            )
            html_lines.append(
                "<a href='{}' target='_blank'><img src='{}' style='{}' /></a>".format(
                    url, img_url, img_style
                )
            )
        else:
            html_lines.append("<div style='{}'>{}</div>".format(txt_style, item))
    html_lines.append("</div>")
    html_str = "".join(html_lines)
    display(HTML(html_str))
