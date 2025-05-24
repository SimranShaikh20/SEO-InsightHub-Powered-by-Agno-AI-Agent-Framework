import streamlit as st
import pandas as pd
from api.firecrawl import crawl_website
from api.exa import fetch_keywords
from api.groq import generate_seo_tips
from utils.pdf_generator import create_pdf_report

st.set_page_config(page_title="SEO InsightHub", layout="wide")
st.title("🔍 SEO InsightHub – Analyze, Compare, Optimize")

with st.sidebar:
    st.header("Input Data")
    site_url = st.text_input("Your Website URL", placeholder="https://your-site.com")
    competitors = st.text_input("Competitor URLs (comma-separated)", placeholder="https://comp1.com, https://comp2.com")
    keywords = st.text_input("Relevant Business Keywords (comma-separated)", placeholder="seo tools, local marketing")
    analyze_btn = st.button("Run Analysis")

if analyze_btn and site_url:
    st.success("Fetching data and analyzing SEO metrics...")

    site_data = crawl_website(site_url)
    competitor_urls = [url.strip() for url in competitors.split(",") if url.strip()]
    competitor_data = [crawl_website(url) for url in competitor_urls]

    # Process keywords input string into a list
    keyword_list = [kw.strip() for kw in keywords.split(",") if kw.strip()]
    keyword_response = fetch_keywords(keyword_list)  # Expecting dict with trending_keywords and search_volume

    trending_keywords = keyword_response.get("trending_keywords", [])
    search_volume = keyword_response.get("search_volume", {})

    keyword_data = [
        {"keyword": kw, "search_volume": search_volume.get(kw, "N/A")}
        for kw in trending_keywords
    ]

    ai_tips = generate_seo_tips(site_data)

    st.subheader("🔎 SEO Scorecard Comparison")
    df = pd.DataFrame([site_data] + competitor_data)
    st.dataframe(df)

    st.subheader("📈 Trending Keywords")
    if keyword_data:
        k_df = pd.DataFrame(keyword_data)
        st.bar_chart(k_df.set_index("keyword"))
    else:
        st.warning("No keyword data available")

    st.subheader("🤖 AI-Generated SEO Tips")
    for tip in ai_tips:
        st.markdown(f"- {tip}")

    # Generate PDF once analysis is done
    report_path = create_pdf_report(site_data, competitor_data, ai_tips)
    with open(report_path, "rb") as f:
        pdf_bytes = f.read()

    # Show download button directly
    st.download_button(
        label="📄 Download SEO Report as PDF",
        data=pdf_bytes,
        file_name="SEO_InsightHub_Report.pdf",
        mime="application/pdf"
    )

else:
    st.info("Enter your website, competitors, and keywords to begin.")
