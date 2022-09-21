// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import { useTable } from 'react-table'
import CONFIG from '../../utils';


export default function Table({ columns, data }) {
    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,
        rows,
        prepareRow
    } = useTable({
        columns, data
    });

    return (
        <>
            {data &&


                <div className="flex flex-col">
                    <div className="overflow-x-auto sm:-mx-6 lg:-mx-8">
                        <div className="py-2 inline-block min-w-full sm:px-6 lg:px-8">
                            <div className="overflow-hidden">

                                <table className="min-w-full">
                                    <thead className="border-b">
                                        {headerGroups.map((headerGroup) => (
                                            <tr {...headerGroup.getHeaderGroupProps()}>
                                                {headerGroup.headers.map((column) => (
                                                    <th {...column.getHeaderProps()} scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                                        {column.render("Header")}
                                                    </th>
                                                ))}
                                            </tr>
                                        ))}
                                    </thead>
                                    <tbody {...getTableBodyProps()}>
                                        {rows.map((row) => {
                                            prepareRow(row);
                                            return (
                                                <tr {...row.getRowProps()} className="border-b">
                                                    {row.cells.map((cell) => {
                                                        if (cell["column"]['Header'].toLowerCase().includes('url')) {
                                                            const cell_obj = cell.render('Cell')['props']['value']
                                                            let url = ''
                                                            if (cell["column"]['Header'] === 'Short Url') {
                                                                url = `${CONFIG.BACKEND_URL}/${cell_obj}`
                                                            } else {
                                                                url = cell_obj
                                                            }
                                                            return <td {...cell.getCellProps()} className="px-6 py-4 text-sm font-medium text-blue-900"><a href={url} target="_blank" rel="noreferrer">{url}</a></td>
                                                        }
                                                        return <td {...cell.getCellProps()} className="px-6 py-4 text-sm font-medium text-gray-900">{cell.render("Cell")}</td>;
                                                    })}

                                                </tr>
                                            );
                                        })}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div >

            }
        </>
    );
};