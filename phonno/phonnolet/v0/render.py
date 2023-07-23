import IPython
from IPython.display import display, HTML


def _transform_to_style_attr(style_object):
    style = ""
    for key, value in style_object.items():
        style += "{}:{};".format(key, value)
    return style.strip()


def _get_anno_txt_style(type):
    if type == "query":
        return _transform_to_style_attr(
            {
                "display": "inline-block",
                "margin": "3px 0",
            }
        )


def _get_anno_img_style(type):
    if type == "query":
        return _transform_to_style_attr(
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
    elif type == "result":
        return _transform_to_style_attr(
            {
                "position": "absolute",
                "object-fit": "contain",
                "width": "100%",
                "height": "100%",
                "user-select": "none",
                "z-index": 999,
                "opacity": 1,
            }
        )


def _get_anno_container_style(type, indent):
    margin_l = "24px" if indent else "0px"
    margin_tb = "4px" if indent else "0px"
    if type == "query":
        return _transform_to_style_attr(
            {
                "display": "flex",
                "gap": "4px",
                "align-items": "flex-end",
                "margin-left": margin_l,
                "margin-top": margin_tb,
                "margin-bottom": margin_tb,
            }
        )
    elif type == "result":
        return _transform_to_style_attr(
            {
                "display": "grid",
                "width": "100%",
                "max-width": "1000px",
                "grid-auto-rows": "1fr",
                "grid-template-columns": "repeat(10,minmax(0,1fr))",
                "height": "auto",
                "gap": "2px",
                "margin-left": margin_l,
                "margin-top": margin_tb,
                "margin-bottom": margin_tb,
            }
        )
    elif type == "text":
        return _transform_to_style_attr(
            {
                "display": "block",
                "width": "100%",
                "max-width": "1000px",
                "padding": "8px 0",
                "margin-left": margin_l,
                "margin-top": margin_tb,
                "margin-bottom": margin_tb,
            }
        )


def _get_anno_anchor_style(type):
    if type == "result":
        return _transform_to_style_attr(
            {
                "display": "block",
                "position": "relative",
                "cursor": "pointer",
                "background": "hsla(0,0%,100%,.98)",
                "border-radius": "2px",
                "text-decoration": "none",
            }
        )


def _get_anno_anchor_content_style(type):
    if type == "result":
        return _transform_to_style_attr(
            {
                "display": "block",
                "content": '""',
                "width": 0,
                "padding-bottom": "100%",
            }
        )


def _get_anno_anchor_content_image_style(type):
    if type == "result":
        return _transform_to_style_attr(
            {
                "position": "absolute",
                "margin": "6px",
                "width": "calc(100% - 12px)",
                "height": "calc(100% - 12px)",
                "background-color": "#fff",
                "border-radius": "1px",
            }
        )


def _get_anno_anchor_content_image_wrap_style(type):
    if type == "result":
        return _transform_to_style_attr(
            {
                "position": "relative",
                "width": "100%",
                "height": "100%",
            }
        )


def _get_anno_anchor_content_image_background_style(type, img_url):
    if type == "result":
        return _transform_to_style_attr(
            {
                "position": "absolute",
                "object-fit": "cover",
                "width": "100%",
                "height": "100%",
                "border-radius": "1px",
                "opacity": 0.25,
                "pointer-events": "none",
                "z-index": 998,
                "background-size": "cover",
                "background-position": "center center",
                "background-repeat": "no-repeat",
                "background-image": "url({})".format(img_url),
            }
        )


def show_annotations(items, origin="", style="query", indent=False):
    root_style = _get_anno_container_style(style, indent)
    img_style = _get_anno_img_style(style)
    txt_style = _get_anno_txt_style(style)
    html_lines = []
    html_lines.append("<div data-name='annotations' style='{}'>".format(root_style))
    for idx, item in enumerate(items):
        if isinstance(item, list) and len(item) == 2:
            item.append({})
        if style == "query":
            if isinstance(item, list):
                [image_id, anno_id, metadata] = item
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
        elif style == "result":
            if not isinstance(item, list):
                continue
            [image_id, anno_id, metadata] = item
            url = "{}/{}#a{}".format(origin, image_id, int(anno_id) + 1)
            img_url = "{}/api/data/annotations_images?imageId={}&annoId={}".format(
                origin, image_id, str(anno_id)
            )

            html_lines.append("<div data-name='annotation'>")  # 0
            html_lines.append(
                "<a href='{}' style='{}' title='{}' target='_blank'>".format(
                    url, _get_anno_anchor_style(style), idx
                )
            )
            html_lines.append(
                "<div style='{}'>".format(_get_anno_anchor_content_style(style))
            )  # 1
            html_lines.append(
                "<div style='{}'>".format(_get_anno_anchor_content_image_style(style))
            )  # 2
            html_lines.append(
                "<div style='{}'>".format(
                    _get_anno_anchor_content_image_wrap_style(style)
                )
            )  # 3
            html_lines.append(
                "<div style='{}'>".format(
                    _get_anno_anchor_content_image_background_style(style, img_url)
                )
            )  # 4
            html_lines.append("</div>")  # 4
            html_lines.append(
                "<img loading='eager' src='{}' style='{}' />".format(img_url, img_style)
            )
            html_lines.append("</div>")  # 3
            html_lines.append("</div>")  # 2
            html_lines.append("</div>")  # 1
            html_lines.append("</a>")
            html_lines.append("</div>")  # 0
    html_lines.append("</div>")
    html_str = "".join(html_lines)
    display(HTML(html_str))


def show_chat(data, origin="", q=False, a=False):
    chat_id = data["chatId"]
    chat_uri = "{}/share/{}".format(origin, chat_id)
    display(
        HTML("<div><a href='{}' target='_blank'>{}</a></div>".format(chat_uri, chat_id))
    )
    if q:
        query = []
        for item in data["qRaw"]:
            if item["type"] == "annotation":
                query.append([item["imageId"], int(item["annoId"])])
            elif item["type"] == "text":
                query.append(item["text"])
        show_annotations(query, origin=origin, style="query", indent=True)
    if a:
        html_lines = []
        html_lines.append(
            "<div data-name='text' style='{}'>".format(
                _get_anno_container_style("text", indent=True)
            )
        )
        html_lines.append("<div>{}</div>".format(data["aRaw"]))
        html_lines.append("</div>")
        html_str = "".join(html_lines)
        display(HTML(html_str))

        annos = []
        for annoKey in data["hitDocs"].keys():
            anno = data["hitDocs"][annoKey]
            annos.append([anno["imageId"], int(anno["annoId"])])
        show_annotations(annos, origin=origin, style="result", indent=True)

    display(
        HTML(
            "<div data-name='spacer' style='{}' />".format("height: 40px; width: 1px;")
        )
    )
