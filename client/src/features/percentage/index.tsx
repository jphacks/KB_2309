import { PieChart } from 'react-minimal-pie-chart';
import { Text, Heading } from '@chakra-ui/react'
import { ArrowDownIcon } from '@chakra-ui/icons'

function Percentage(props: { title: string, percentage: number, result: string, color: string }) {
    const data = [
        { title: 'Good', value: props.percentage, color: '#E38627' },
        { title: 'Bad', value: 100-props.percentage, color: '#C13C37' },
    ];

    return (
        <div style={{marginTop: "150px"}}>
            {/* <Text fontSize="4xl">{props.title}</Text> */}
            <Heading style={{marginBottom: "10px"}}>{props.title}</Heading>
            <PieChart 
                data={data}
                label={({ dataEntry }) => `${dataEntry.title}: ${dataEntry.value}`}
                labelStyle={{ fontSize: '7px', color: 'white', fontStyle: 'bold' }}
                style={{ height: '300px' }}
            />
            <ArrowDownIcon w={16} h={16} color="red.500" />
            <Heading>{props.result}</Heading>
        </div>       
    );
}

export default Percentage;
