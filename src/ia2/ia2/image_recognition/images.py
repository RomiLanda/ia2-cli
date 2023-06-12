import pdf2image
import glob
import cv2
import numpy as np
import layoutparser as lp
from PIL import Image
import warnings

warnings.filterwarnings("ignore")


def create_image_from_pdf(pdf_path: str, OUTPUT_PATH: str):
    pdf2image.convert_from_path(
        pdf_path,
        dpi=600,
        output_folder=OUTPUT_PATH,
        fmt="png",
        paths_only=True,
        output_file="image_",
    )[0]


def apply_image_detect(img_array):
    model = lp.Detectron2LayoutModel(
        "lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config",
        extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
        label_map={0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"},
    )
    return model.detect(img_array)


def transform_images(folder_images_path: str):
    """Transforma imagenes de una carpeta en array"""
    images = [
        [cv2.imread(file), file] for file in glob.glob(folder_images_path)
    ]
    imgs_array_info = [
        {"image": np.asarray(image[0]), "path": image[1]} for image in images
    ]
    return imgs_array_info


def classifier(imgs_array_info):
    """Return True si hay figura"""
    layuout = apply_image_detect(imgs_array_info["image"])
    for ly in layuout.get_info("type"):
        if ly == "Figure":
            return True
        else:
            return False


def get_figure_boxes(img_array_info):
    df_lyt = apply_image_detect(img_array_info["image"]).to_dataframe()
    df_lyt_fig = df_lyt[df_lyt["type"] == "Figure"]
    d = df_lyt_fig.to_dict()
    box = {
        "x_1": int(d["x_1"][0]),
        "y_1": int(d["y_1"][0]),
        "x_2": int(d["x_2"][0]),
        "y_2": int(d["y_2"][0]),
    }
    img_array_info["box"] = box
    return img_array_info


def face_recognition(img_info):
    face_cascade = cv2.CascadeClassifier(
        "/resources/datasets/image_recognition/haarcascade_frontalface_default.xml"
    )
    fig = img_info["image"][
        img_info["box"]["y_1"] : img_info["box"]["y_2"],
        img_info["box"]["x_1"] : img_info["box"]["x_2"],
    ]
    gray = cv2.cvtColor(fig, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    img_info["box_img"] = fig
    img_info["faces_box"] = faces
    return img_info


def blurear_(img_array):
    for (x, y, w, h) in img_array["faces_box"]:
        area_color = img_array["box_img"][y : y + h, x : x + w]
        blur = cv2.GaussianBlur(area_color, (1001, 1001), 0)
        img_array["box_img"][y : y + h, x : x + w] = blur
    return img_array


def save_page_image(img_array):
    im = Image.fromarray(img_array["image"])
    im.save(img_array["path"])


def create_pdf(folder_images_path: str, path_pdf_blue: str):
    images = [
        Image.open(file) for file in sorted(glob.glob(folder_images_path))
    ]
    images[0].save(
        path_pdf_blue,
        "PDF",
        resolution=100.0,
        save_all=True,
        append_images=images[1:],
    )
