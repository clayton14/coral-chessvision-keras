import src.utils as utl
import src.test_model as test_model

# from pathlib import Path
import os


def test_paths():
    print("root: ", utl.get_root_dir())
    print("models: ", utl.get_modles_dir())
    print("test_imgs: ", utl.get_test_imgs_dir())
    print("datsets: ", utl.get_datasets_dir())


# test modles
def main():
    MODLES = os.listdir(utl.get_modles_dir())
    print(MODLES)

    print(os.path.join(utl.get_modles_dir(), MODLES[0]))

    # test_model.pt_to_onnx(
    #     os.path.join(utl.get_modles_dir(), MODLES[0]), "best_transformed_dection.onnx"
    # )



    test_paths()

    test_model.test_image()
    

if __name__ == "__main__":
    main()
