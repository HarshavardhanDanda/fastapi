# Files
from typing import Union, List

from fastapi import FastAPI, File, UploadFile
from typing_extensions import Annotated

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# UploadFile has the following attributes:
#
# filename: A str with the original file name that was uploaded (e.g. myimage.jpg).
# content_type: A str with the content type (MIME type / media type) (e.g. image/jpeg).
# file: A SpooledTemporaryFile (a file-like object). This is the actual Python file that you can pass directly to other functions or libraries that expect a "file-like" object.
# UploadFile has the following async methods.
# They all call the corresponding file methods underneath (using the internal SpooledTemporaryFile).
#
# write(data): Writes data (str or bytes) to the file.
# read(size): Reads size (int) bytes/characters of the file.
# seek(offset): Goes to the byte position offset (int) in the file.
# E.g., await myfile.seek(0) would go to the start of the file.
# This is especially useful if you run await myfile.read() once and then need to read the contents again.
# close(): Closes the file.


# Optional File Upload

@app.post("/files/")
async def create_file(file: Annotated[Union[bytes, None], File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


# UploadFile with Additional Metadata
@app.post("/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}


# Multiple File Uploads
@app.post("/files/")
async def create_files(files: Annotated[List[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}

