from .UploadSession import UploadSession
from ytb_up import *
from datetime import datetime,date,timedelta
import asyncio

# # for cookie issue,
# upload = Upload(
# )

async def startUpload(profilepath="",proxy_option="",watcheveryuploadstep=True,CHANNEL_COOKIES='',username='',password='',recordvideo=True):

    return Upload(
        # use r"" for paths, this will not give formatting errors e.g. "\n"
        root_profile_directory=profilepath,
        proxy_option=proxy_option,
        watcheveryuploadstep=watcheveryuploadstep,
        # if you want to silent background running, set watcheveryuploadstep false
        CHANNEL_COOKIES=CHANNEL_COOKIES,
        username=username,
        password=password,
        recordvideo=recordvideo
        # for test purpose we need to check the video step by step ,
    )
async def instantpublish(uploadSession:UploadSession,upload:Upload):

    await upload.upload(
        videopath=uploadSession.videopath,
        title=uploadSession.title,
        description=uploadSession.des,
        thumbnail=uploadSession.thumbpath,
        tags=uploadSession.tags,
        closewhen100percentupload=True,
        publish_date=uploadSession.publish_date,
        publishpolicy=1
    )

async def privatedraft(uploadSession:UploadSession,upload:Upload):
    await upload.upload(
        videopath=uploadSession.videopath,
        title=uploadSession.title,
        description=uploadSession.des,
        thumbnail=uploadSession.thumbpath,
        tags=uploadSession.tags,
        closewhen100percentupload=True,
        publish_date=uploadSession.publish_date,
        publishpolicy=0
    )





async def scheduletopublish_specific_date(uploadSession:UploadSession,upload:Upload):
        # mode a:release_offset exist,publishdate exist will take date value as a starting date to schedule videos
        # mode b:release_offset not exist, publishdate exist , schedule to this specific date
        # mode c:release_offset not exist, publishdate not exist,daily count to increment schedule from tomorrow
        # mode d: offset exist, publish date not exist, daily count to increment with specific offset schedule from tomorrow         

    # publish_date = datetime.strftime(publish_date, "%Y-%m-%d %H:%M:%S")
    await upload.upload(
        videopath=uploadSession.videopath,
        title=uploadSession.title,
        description=uploadSession.des,
        thumbnail=uploadSession.thumbpath,
        tags=uploadSession.tags,
        closewhen100percentupload=True,
        publish_date=uploadSession.publish_date,
        publishpolicy=2

    )




async def bulk_scheduletopublish_specific_date(videos:list,upload:Upload) -> None:
    """ concurrently upload for multiple video files."""
    print('===',type(videos),type(upload))
    tasks = [
        scheduletopublish_specific_date(uploadSession=video, upload=upload)
        for video in videos
    ]

    await asyncio.gather(*tasks)


async def bulk_privatedraft(videos:list,upload:Upload) -> None:
    """ concurrently upload for multiple video files."""
    tasks = [privatedraft(uploadSession=video, upload=upload) for video in videos]
    await asyncio.gather(*tasks)

async def bulk_instantpublish(videos:list,upload:Upload) -> None:
    """ concurrently upload for multiple video files."""
    tasks = [
        instantpublish(uploadSession=video, upload=upload) for video in videos
    ]

    await asyncio.gather(*tasks)

