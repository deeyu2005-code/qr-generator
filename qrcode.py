import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="📱")

st.title("📱 QR Code Generator")
st.write("Enter any text or URL and generate a QR code instantly.")

text = st.text_input("Enter text or URL")

if st.button("Generate QR Code"):
    if text:
        qr = qrcode.make(text)

        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        st.image(buffer, caption="Generated QR Code")

        st.download_button(
            label="⬇ Download QR Code",
            data=buffer.getvalue(),
            file_name="QRCode.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter some text.")
        