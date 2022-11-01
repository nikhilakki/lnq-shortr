// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import Sidebar from './Sidebar'


const Layout = ({ children }) => {
    return (
        <>
            <Sidebar />
            <div className="ml-auto mb-6 lg:w-[75%] xl:w-[80%] 2xl:w-[85%]">
                <div className="sticky z-10 top-0 h-16 border-b bg-white lg:py-2.5">
                    <div className="px-6 py-9 flex items-center justify-between space-x-4 2xl:container">
                        {children}
                    </div>
                </div>
            </div>
        </>
    );
};

export default Layout;