from django.contrib import admin
from backend.app.models import Post
from mptt.admin import MPTTModelAdmin

class PostAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ["id","user", "text", 'parent',"date",'like']
    #list_filter = ["date"]

admin.site.register(Post, PostAdmin)


#from django.contrib import admin
#from mptt.admin import DraggableMPTTAdmin
#from backend.app.models import Post
#
# admin.site.register(
#     Post,
#     DraggableMPTTAdmin,
#     list_display=(
#         'tree_actions',
#         'indented_title',
#         'user',
#         'text',
#         'parent',
#         'date',
#
#     ),
#     list_display_links=(
#         'indented_title',
#     ),
# )
