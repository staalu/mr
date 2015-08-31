Loadplugin("D:\avs\plugins\MP_Pipeline.dll")

MP_Pipeline("""
SetmemoryMAX(1280)
LoadPlugin("D:\avs\plugins\xy-VSFilter.dll")
Loadplugin("D:\avs\plugins\ffms2.dll")
Import("D:\avs\plugins\ffms2-2.18-rc1\FFMS2.avsi")

FFmpegSource2("<SOURCE_FILE_PATH_DONOT_EDIT_OR_REMOVE_THIS>")
TextSub("<SUBTITLE_FILE_PATH_DONOT_EDIT_OR_REMOVE_THIS>")

lanczosresize(1280,720)
### prefetch: 16, 0
### ###
""")