import * as React from 'react';
import Link from "next/link";
import { useTheme } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Zoom from '@mui/material/Zoom';
import Box from '@mui/material/Box';
import { SxProps } from '@mui/system';
import { Button, Card, CardActionArea, CardContent, CardMedia, Stack } from '@mui/material';
import Modal from '@mui/material/Modal';

const style = {
  position: 'absolute' as 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  boxShadow: 24,
  p: 4,
};



interface TabPanelProps {
  children?: React.ReactNode;
  dir?: string;
  index: number;
  value: number;
}


function a11yProps(index: any) {
  return {
    id: `action-tab-${index}`,
    'aria-controls': `action-tabpanel-${index}`,
  };
}

const fabStyle = {
  position: 'absolute',
};

export default function Searching() {
  const theme = useTheme();
  const [value, setValue] = React.useState(0);

  const handleChange = (event: unknown, newValue: number) => {
    setValue(newValue);
  };


  const transitionDuration = {
    enter: theme.transitions.duration.enteringScreen,
    exit: theme.transitions.duration.leavingScreen,
  };
  

  const fabs = [
    {
      exc: ['10', '20', '30'],
      sx: fabStyle as SxProps,
      label: 'Add',
    },
    {
      exc :  ['55', '99', '60'],
      sx: fabStyle as SxProps,
      label: 'Edit',
    },
  ];
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Text in a modal
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
          </Typography>
        </Box>
      </Modal>
          <>
      <Typography variant="h5">
      유형별 맞춤정책 찾아보기
      </Typography>
      <br />
      </>

      <Box
        sx={{
          bgcolor: 'background.paper',
          position: 'relative',
          minHeight: 200,
        }}
      >
        <AppBar position="static" color="default">
          <Tabs
            value={value}
            onChange={handleChange}
            indicatorColor="primary"
            textColor="primary"
            variant="fullWidth"
            aria-label="action tabs example"
          >
            <Tab label="중소기업" {...a11yProps(0)} />
            <Tab label="청년정책" {...a11yProps(1)} />
          </Tabs>
        </AppBar>
<br />

        {fabs.map((fab, index) => (
        <Zoom
          key={fab.exc}
          in={value === index}
          timeout={transitionDuration}
          unmountOnExit
        >
           <Box sx={fab.sx}>
            {fab.exc.map((exc, index) => (
              <Button>
                {exc}
              </Button>     
            ))}

            
            <Stack direction="row">
              {fab.exc.map((exc, index) => (
              <Card 
              onClick={handleOpen}
              sx={{ 
                m : 3,
                maxWidth: 345 }}>
                <CardActionArea>
                  <CardMedia
                    component="img"
                    height="100"
                    image="/images/ci.png"
                    alt="green iguana"
                  />
                  <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                      {exc}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                    청년정책어쩌구저쩌구청년정책어쩌구저쩌구청년정책어쩌구저쩌구청년정책어쩌구저쩌구청년정책어쩌구저쩌구청년정책어쩌구저쩌구청년정책어쩌구저쩌구
                    </Typography>
                  </CardContent>
                </CardActionArea>
              </Card> 
            ))}
            </Stack>
          </Box>

        </Zoom>
        ))}
      </Box>
    </>
  );
}