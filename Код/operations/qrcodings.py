import qrcode
import cv2


class qr_code:
    def create_qr_code(text):
        """
        Create a QR code image based on the given text.

        Args:
            text (str): The text to encode in the QR code.

        Returns:
            img (qrcode.image.pil.PilImage): The QR code image.
        """
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            return img
        except Exception:
            return f"Too much data to create"

    def read_qr_code(filename):
        """
        Read a QR code image and decode the data.

        Args:
            filename (str): The path to the QR code image file.

        Returns:
            decoded_text (str): The decoded text from the QR code.
        """
        try:
            image = cv2.imread(filename)
            detector = cv2.QRCodeDetector()
            data, pts, qrcode = detector.detectAndDecode(image)
            if data:
                decoded_text = data
                return decoded_text
            else:
                return f"Too much data to read"
        except Exception:
            return f"Impossible to read"
