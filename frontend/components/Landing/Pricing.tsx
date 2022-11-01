// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import Image from "next/image"

const Pricing = () => {
    return (
        <section id="pricing" className="bg-white dark:bg-gray-900">
            <div className="gap-16 items-center py-8 px-4 mx-auto max-w-screen-xl lg:grid lg:grid-cols-2 lg:py-16 lg:px-6">
                <div className="font-light text-gray-500 sm:text-lg dark:text-gray-400">
                    <h2 className="mb-4 text-4xl font-extrabold text-gray-900 dark:text-white">Pricing</h2>
                    <p className="mb-4">SaaS version is <strong>free</strong> until beta phase and don't you worry there will be a free tier in the future 😃</p>
                    <p className="mb-4"></p>
                    <p className="mb-4 italic">Generate upto 1k short links per account</p>
                </div>
                <div className="grid grid-cols-2 gap-4 mt-8">
                    <Image className="w-full rounded-lg" src="/images/Group Members-1.png" width="1200px" height="852px" alt="office content 1" />
                </div>
            </div>
        </section>
    );
};

export default Pricing;