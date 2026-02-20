from pathlib import Path
import zipfile

class Get_Data_From_Blender_API_Zip ():

    def __init__(self, blender_api_zip_path : str):
        self.zip: Path = Path(blender_api_zip_path)
        self.folder : Path

    def get_folder_from_zip (self):
        try :
            with zipfile.ZipFile(self.zip, "r") as z:
                z.extractall("/unzipped_files")
        except :
            raise RuntimeError("Could not extract zip file")


    def get_files_lists_from_folder (self) :

        return 0