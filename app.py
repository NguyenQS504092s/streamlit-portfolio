import streamlit as st
from PIL import Image
import os
import base64

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Portfolio | Nguyen Quang Sang",
    page_icon="✨",
    layout="wide"
)

# --- HELPER FUNCTIONS ---
def load_css(file_path):
    """Injects a CSS file into the Streamlit app."""
    if os.path.exists(file_path):
        with open(file_path) as f:
            return f.read()
    st.warning(f"CSS file not found at {file_path}. Styling will be incorrect.")
    return ""

def get_base64_image(image_path):
    """Encodes an image to base64."""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return "" # Return empty string if file not found

# --- PATHS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
CSS_PATH = "E:\\Github_Repos\\My-portfolio\\nextjs-portfolio\\src\\app\\globals.css"

# --- INJECT CUSTOM CSS ---
st.markdown(f"<style>{load_css(CSS_PATH)}</style>", unsafe_allow_html=True)

# --- MAIN APP ---

# --- HERO SECTION ---
st.markdown("""
<div class="hero-text">
    <div class="title-badge">Computer Science, Major in AI </div>
    <h1>Nguyen Quang Sang</h1>
    <p>Passionate AI/ML engineer and data scientist. Let’s build something great!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- PROFILE & SKILLS ---
st.header("👨‍💻 About Me & Skills")
col1, col2 = st.columns([1, 2])
with col1:
    profile_img_b64 = get_base64_image(os.path.join(IMAGE_DIR, "profile-picture.jpg"))
    st.markdown(f'<img src="data:image/jpeg;base64,{profile_img_b64}" class="profile-picture">', unsafe_allow_html=True)
with col2:
    st.write("Passionate AI/ML engineer and data scientist with expertise in building scalable machine learning models, data analysis, and computer vision applications.")
    st.subheader("Experience")
    st.write("- Machine Learning Engineer at XYZ Corp (2026 - Present)")
    st.write("- Data Scientist Intern at ABC Ltd (2020 - 2021)")
    st.subheader("Education")
    st.write("- Bachelor in Artificial Intelligence - Computer Science, FPT University (2023 - 2027)")
    st.write("- M.S in Computer Science, Tech University (2027 - 2029)")
    with st.expander("AI / Machine Learning"):
        st.write("- Supervised & unsupervised learning\n- Regression, classification\n- Model tuning and evaluation")
    with st.expander("Deep Learning"):
        st.write("- Neural networks, CNN, RNN\n- Transfer learning\n- Frameworks: TensorFlow, PyTorch")
    with st.expander("Data Science"):
        st.write("- Data wrangling and visualization\n- Statistical analysis\n- Pandas, NumPy, Matplotlib")
    with st.expander("Computer Vision"):
        st.write("- Image classification and detection\n- OpenCV, YOLO\n- Semantic segmentation")
    with st.expander("DevOps"):
        st.write("- CI/CD pipelines\n- Docker, Kubernetes\n- Cloud platforms: AWS, GCP, Azure\n- Monitoring & logging")
    with st.expander("MLOps"):
        st.write("- Model deployment\n- Model monitoring & versioning\n- ML pipelines with Kubeflow / MLflow\n- Scalable model serving")
    
    
st.markdown("---")

# --- PROJECTS ---
st.header("🚀 Projects")
st.subheader("1. Real-time Object Detection")
st.write("Deployed YOLOv5 on edge devices to detect objects in real-time.")
project1_b64 = get_base64_image(os.path.join(IMAGE_DIR, "project-1.png"))
if project1_b64:
    st.markdown(f'<img src="data:image/png;base64,{project1_b64}" style="width: 100%; border-radius: 8px; margin-top: 15px;" />', unsafe_allow_html=True)
st.markdown("[🔗 GitHub Repo](https://github.com)")
st.subheader("2. Predictive Maintenance with IoT")
st.write("Built ML models using time-series data from industrial sensors to predict potential failures. Integrated with MQTT for real-time alerts and dashboard visualization.")
st.markdown("[🔗 GitHub Repo](https://github.com)")
project2_b64 = get_base64_image(os.path.join(IMAGE_DIR, "project-2.png"))
if project2_b64:
    st.markdown(f'<img src="data:image/png;base64,{project2_b64}" style="width: 100%; border-radius: 8px; margin-top: 15px;" />', unsafe_allow_html=True)
st.markdown("---")

# --- Datasets ---
st.header("📊 Datasets (Kaggle)")
dataset1_b64 = get_base64_image(os.path.join(IMAGE_DIR, "kaggle1.png"))
if dataset1_b64:
    st.markdown(f'<img src="data:image/png;base64,{dataset1_b64}" style="width: 100%; border-radius: 8px; margin-top: 15px;" />', unsafe_allow_html=True)
st.subheader("1. Titanic - Machine Learning from Disaster")
st.write("Classic binary classification dataset. Explored survival prediction using logistic regression, decision trees, and ensemble models.")
st.markdown("[🔗 Kaggle Dataset](https://www.kaggle.com/c/titanic)")
st.markdown("---")
st.subheader("2. House Prices - Advanced Regression Techniques")
dataset2_b64 = get_base64_image(os.path.join(IMAGE_DIR, "kaggle2.png"))
if dataset2_b64:
    st.markdown(f'<img src="data:image/png;base64,{dataset2_b64}" style="width: 100%; border-radius: 8px; margin-top: 15px;" />', unsafe_allow_html=True)
st.write("Used feature engineering and ensemble regressors (XGBoost, Lasso) to predict house prices from rich tabular data.")
st.markdown("[🔗 Kaggle Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)")

# --- RESEARCH & PUBLICATIONS ---
st.header("📚 Research & Publications")
paper1_b64 = get_base64_image(os.path.join(IMAGE_DIR, "paper1.png"))
st.subheader("1. A Lightweight Deep Learning Framework for Real-Time Defect Detection")
st.write("Published at IEEE ICMLC 2023. Proposed a compact CNN for detecting surface anomalies.")
if paper1_b64:
    st.markdown(f'<img src="data:image/png;base64,{paper1_b64}" style="width: 100%; border-radius: 8px; margin-top: 15px;" />', unsafe_allow_html=True)
st.markdown("[🔗 Publication Link](https://ieeexplore.ieee.org/document/example123)")
st.subheader("2. Blog: Predicting Stock Prices using LSTM & Attention")
st.write("Technical blog post explaining how to combine LSTM and attention mechanisms for forecasting financial time series.")
st.markdown("[🔗 Read Blog](https://medium.com)")
paper2_b64 = get_base64_image(os.path.join(IMAGE_DIR, "paper2.png"))
if paper2_b64:
    st.markdown(f'<img src="data:image/png;base64,{paper2_b64}" style="width: 100%; border-radius: 8px; margin-top: 15px;" />', unsafe_allow_html=True)

st.markdown("---")

# --- CERTIFICATIONS ---
st.header("📜 Certifications")
cert_dl_b64 = get_base64_image(os.path.join(IMAGE_DIR, "certificate_dl.png"))
st.subheader("Deep Learning Specialization - Coursera")
if cert_dl_b64:
    st.markdown(f'<img src="data:image/png;base64,{cert_dl_b64}" style="width: 100%; border-radius: 8px; margin-top: 15px;" />', unsafe_allow_html=True)
st.markdown("[Verify Certificate](https://coursera.org/verify/certificate/example)")
st.subheader("TensorFlow Developer Certificate")
st.markdown("[Verify Certificate](https://www.tensorflow.org/certificate/example)")
cert_tf_b64 = get_base64_image(os.path.join(IMAGE_DIR, "certificate_tf.png"))
if cert_tf_b64:
    st.markdown(f'<img src="data:image/png;base64,{cert_tf_b64}" style="width: 100%; border-radius: 8px; margin-top: 15px;" />', unsafe_allow_html=True)

st.markdown("---")

# --- CONTACT ---
st.header("📬 Contact Me")
st.markdown("""
- **Email:** sangquang2904@gmail.com  
- **LinkedIn:** [linkedin.com/in/nguyễn-quang-sang-068784218](https://linkedin.com/in/nguyễn-quang-sang-068784218)  
- **GitHub:** [github.com/NguyenQS504092s](https://https://github.com/NguyenQS504092s)  
""")