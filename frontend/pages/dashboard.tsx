import { AuthenticatedTemplate, useIsAuthenticated } from "@azure/msal-react"
import Layout from "../components/Dashboard/Layout"
import { useEffect, useMemo, useState } from "react"
import Table from "../components/Dashboard/Table"
import InputBox from "../components/Dashboard/InputBox"
import CONFIG from "../utils"

export default function Dashboard() {
  const [loading, setLoading] = useState(true)
  const [data, setData] = useState([])
  const user = useIsAuthenticated()
  // const router = useRouter()

  const deleteAction = async (id) => {
    const resquestOptions = {
      method: "DELETE",
    }
    const url = `${CONFIG.BACKEND_URL}/short-url/${id}`
    console.log(url)
    await fetch(url, resquestOptions)
  }
  const columns = useMemo(
    () => [
      {
        Header: "ID",
        accessor: "id",
      },
      {
        Header: "Name",
        accessor: "name",
      },
      {
        Header: "Long Url",
        accessor: "url",
      },
      {
        Header: "Short Url",
        accessor: "short_url",
      },
      {
        Header: "Action",
        id: "delete",
        accessor: () => "delete",

        Cell: (tableProps) => (
          <button
            className="flex
                  px-3
                  py-2.5
                  bg-red-600
                  text-white
                  font-medium
                  text-xs
                  leading-tight
                  uppercase
                  rounded
                  shadow-md
                  hover:bg-blue-700 hover:shadow-lg
                  focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
                  active:bg-blue-800 active:shadow-lg
                  transition
                  duration-150
                  ease-in-out"
            onClick={async () => {
              const id = tableProps.row.original.id
              deleteAction(id)
              setLoading(true)
            }}
          >
            X
          </button>
        ),
      },
    ],
    []
  )

  const getData = async () => {
    const response = await fetch(`${CONFIG.BACKEND_URL}/short-url/all`)
      .then((data) => data.json())
      .catch((err) => console.error(err))
    return response
  }

  useEffect(() => {
    const fetchData = async () => {
      const response = await getData()
      setData(response)
    }

    fetchData()
    return () => {
      setLoading(false)
    }
  }, [loading])

  return (
    <AuthenticatedTemplate>
      <>
        {user && (
          <Layout>
            <div className="px-6 pt-6 xl:container">
              <div className="grid gap-1 md:grid-cols-1 lg:grid-cols-1">
                <InputBox loading={loading} setLoading={setLoading} />
              </div>
              <br />
              <div className="grid gap-1 md:grid-cols-1 lg:grid-cols-1">
                <h3 className="flex font-mono m-auto">
                  Short links created by you!
                </h3>

                <Table columns={columns} data={data} />
              </div>
            </div>
          </Layout>
        )}
        {/* {!user && router.push(`${CONFIG.FRONTEND_URL}/`)} */}
      </>
    </AuthenticatedTemplate>
  )
}
