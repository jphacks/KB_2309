import {Card, CardBody, CardFooter, Heading, Image, Stack, Text, Button} from '@chakra-ui/react';

function Comment(props: { text: string }) {
  return (
    <>
    <Card
        direction={{ base: 'column', sm: 'row' }}
        overflow='hidden'
        variant='outline'
        width={{ base: '100%', sm: '100%' }}
    >
    <Image
        objectFit='cover'
        maxW={{ base: '100%', sm: '200px' }}
        src='https://images.unsplash.com/photo-1667489022797-ab608913feeb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw5fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=800&q=60'
        alt='Caffe Latte'
    />

    <Stack>
        <CardBody>
        <Heading size='md'>Feedback Comment</Heading>
        <Text py='2'>{props.text}</Text>
        </CardBody>

        {/* <CardFooter>
        <Button variant='solid' colorScheme='blue'>
            Buy Latte
        </Button>
        </CardFooter> */}
    </Stack>
    </Card>
    </>
  );
}

export default Comment;
