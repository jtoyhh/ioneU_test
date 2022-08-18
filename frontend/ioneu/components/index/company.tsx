import { Container, Grid } from "@mui/material";
import Graph from "./graph";
import HashTag from "./hashtag";
import Searching from "./Search/index";

export default function Company() {
  return (
    <>
      <Container>
        <Grid container spacing={10}>
          <Grid 
            item xs={6}
            // style={{ color: 'white', backgroundColor: '#e91e63' }}
            >
            <HashTag />
          </Grid>
          <Grid item xs={6}>
            <Graph />
          </Grid>
        </Grid>
        <br />
        <br />
        <Grid sx={{
          height: "500px",
        }}>
          <Searching />
        </Grid>
      </Container>
    </>
  )
}