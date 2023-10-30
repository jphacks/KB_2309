import "./index.css"
import { Text, Heading } from '@chakra-ui/react'
import { Search2Icon } from "@chakra-ui/icons";

function Header() {
    return (
        <nav className="nav">
            <ul>
                <li>
                <Search2Icon w={8} h={8} color="white" marginTop={4} marginRight={2}/>
                </li>
                <li>
                <a href="/">
                <Heading>PosturePro / 座ルール</Heading>
                </a>
                </li>
                {/* <li><a href="/questionnare">Rating</a></li> */}
                {/* <li><a href="/result">Result</a></li>
                <li><a href="/admin">Admin</a></li> */}
            </ul>
        </nav>
    )
}

export default Header
