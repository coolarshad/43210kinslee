from django import template
register=template.Library()

@register.simple_tag
def get_first_image(image):
    try:
        first_image_block = image.images[0].value.get('image')
        if first_image_block:
            return first_image_block.file.url
    except IndexError:
        pass  # Handle the case where there are no image blocks or the index is out of range
    except AttributeError:
        pass  # Handle the case where the first block does not have an 'image' attribute
    return ''  # Return an empty string if no image URL is found

@register.simple_tag
def get_first_caption(image):
    try:
        first_caption_block = image.images[0].value.get('caption')
        if first_caption_block:
            return first_caption_block.source
    except IndexError:
        pass  # Handle the case where there are no image blocks or the index is out of range
    except AttributeError:
        pass  # Handle the case where the first block does not have a 'caption' attribute
    return ''  # Return an empty string if no caption text is found