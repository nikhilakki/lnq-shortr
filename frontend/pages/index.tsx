// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import Layout from "../components/Layout";
import Header from "../components/Header";
import Hero from "../components/Hero";
import Feature from '../components/Feature';
import Service from '../components/Service';
import About from '../components/About';
import Footer from '../components/Footer';

const Index = () => {
  return (
    <Layout pageTitle="Landing Page Nextjs">
      <Header />
      <Hero />
      <Feature/>
      <Service />
      <About />
      <Footer />
    </Layout>
  )
}

export default Index;
