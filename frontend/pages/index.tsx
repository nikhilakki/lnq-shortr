// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import Layout from "../components/Layout";
import Header from "../components/Header";
import Hero from "../components/Hero";
import Feature from '../components/Feature';
import About from '../components/About';
import Footer from '../components/Footer';
import Login from '../components/Login';

const Index = () => {
  return (
    <Layout pageTitle="Shorten URL links with lnq-shortr!">
      <Header />
      <Hero />
      <Feature />
      <About />
      <Login />
      <Footer />
    </Layout>
  )
}

export default Index;
