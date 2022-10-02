import React from "react";
import { useNavigate } from "react-router-dom";
import Slider from "../components/Slider";
import Layout from "./../components/Layout/Layout";
import "../styles/homepage.css";

const HomePage = () => {
  const navigate = useNavigate();
  const img1 =
    "https://media.istockphoto.com/photos/agriculture-farmer-gesturing-in-wheat-field-with-thumbs-up-picture-id498549410?k=6&m=498549410&s=612x612&w=0&h=BFVb82GryPU0Wyshf46rJS43feCxZKt8rF8gXARToTI=";
  const img2 =
    "https://miro.medium.com/max/1432/1*8HRpR3YcffW_WEYEZ5RSHw.jpeg";
  return (
    <Layout>
      <Slider />
      <div className="home-cat row d-flex align-items-center justify-content-center">
        <h1>Category</h1>
        <div className="col-md-5 ">
          <div className="Imagecontainer">
            <img src={img1} alt="Rent" style={{ width: "100%" }} />
            <button className="btn" onClick={() => navigate("/category/rent")} style={{ width: "100%" }} >
              Young and Happy Farmer
            </button>
          </div>
        </div>
        <div className="col-md-5">
          <div className="Imagecontainer">
            <img src={img2} alt="Rent" style={{ width: "100%" }} />
            <button className="btn" onClick={() => navigate("/category/sale")} style={{ width: "100%" }}>
              Disease Detection in Plants
            </button>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default HomePage;
