// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import { useUser } from '@auth0/nextjs-auth0';
import Layout from '../components/Dashboard/Layout';


const Account = () => {
    const { user, error, isLoading } = useUser();

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>{error.message}</div>;
    return (
        <Layout>
            <div className="px-6 pt-6 2xl:container">
                <div className="grid gap-6 md:grid-cols-3 lg:grid-cols-3">
                    <div>
                        <div className="h-full py-6 px-6 rounded-xl border border-gray-200 bg-white">
                            <div className="my-8">
                                <h1 className="text-3xl font-bold text-gray-800">{user ? user.name : "Dummy"}</h1>
                                <span className="text-gray-500">{user ? user.email : "Admin"}</span>
                            </div>
                            <h5 className="text-xl text-gray-700">Quota Usage <em>(coming soon...)</em></h5>
                            <div className="my-8">
                                <h1 className="text-5xl font-bold text-gray-800">1%</h1>
                                <span className="text-gray-500">of total limit of 1000</span>
                            </div>
                            <table className="mt-6 -mb-2 w-full text-gray-600">
                                <tbody>
                                    <tr>
                                        <td className="py-2">Links generated</td>
                                        <td className="text-gray-500">100</td>
                                    </tr>
                                    <tr>
                                        <td className="py-2">Total Capacity</td>
                                        <td className="text-gray-500">1000</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>

    )
}

export default Account