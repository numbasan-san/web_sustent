
from wagtail_blocks.blocks import struct_block as blocks

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(require = True, help_text = "Add your title")

    content = blocks.ListBlock(
        blocks.StructBlock(
            ('title', blocks.TextBlock(required = True))
        )
    )