import os
import re
import tarfile
import zipfile

class ARCHIVE_TYPES:
    ZIP = "zip"
    TAR = "tar"


class Unzipper:
    def __init__(self):
        self.map_types = {
            "tar": {
                "type": ARCHIVE_TYPES.TAR,
                "keys": "r:"
            },
            "tar.gz": {
                "type": ARCHIVE_TYPES.TAR,
                "keys": "r:gz"
            },
            "zip": {
                "type": ARCHIVE_TYPES.ZIP,
                "keys": None
            },
            "gzip": {
                "type": ARCHIVE_TYPES.TAR,
                "keys": 'r:gz'
            }
        }

    def extract(self, filename, output=None, *args, **kwargs):
        for (extension, params) in self.map_types.items():
            if filename.endswith(extension):
                if params["type"] == ARCHIVE_TYPES.TAR:
                    return self.extract_tar(filename, output, params, *args, **kwargs)

                if params["type"] == ARCHIVE_TYPES.ZIP:
                    return self.extract_zip(filename, output, *args, **kwargs)

    def extract_tar(self, file, output=None, params=None, callback=None):
        output = output if output else self.convert_zip_to_output_filename(file, 2)
        tar = tarfile.open(file, params["keys"])

        members = tar.getmembers()
        total_length, dl = len(members), 0

        if callback:
            callback(0)

        for member in members:
            dl += 1
            percent = dl / total_length

            if callback:
                callback(percent)

            tar.extract(member, path=output)

        tar.close()
        return output

    def extract_zip(self, file, output=None, callback=None):
        output = output if output else self.convert_zip_to_output_filename(file)
        self.mkdir(output)

        zf = zipfile.ZipFile(file)
        total_length, dl = sum((file.file_size for file in zf.infolist())), 0

        if callback:
            callback(0)

        for file in zf.infolist():
            dl += file.file_size
            percent = dl / total_length

            if callback:
                callback(percent)

            zf.extract(file, output)

        return output

    @staticmethod
    def convert_zip_to_output_filename(file, key=1):
        return re.findall(re.compile(r"(.*)(?:\..*){" + str(key) + "}"), file)[0]

    def mkdir(self, path):
        try:
            os.mkdir(path)
        except:
            pass
        return 0
