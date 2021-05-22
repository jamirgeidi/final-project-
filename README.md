
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>.</title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
      * {
        box-sizing: border-box;
      }

      /* Style the body */
      body {
        font-family: Arial, Helvetica, sans-serif;
        margin: 0;
      }

      /* Header/logo Title */
      .header {
        padding: 80px;
        text-align: center;
        background: green;
        color: white;
      }

      /* Increase the font size of the heading */
      .header h1 {
        font-size: 50px;
      }

      /* Style the top navigation bar */
      .navbar {
        overflow: hidden;
        background-color: black;
      }

      /* Style the navigation bar links */
      .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
      }

      /* Right-aligned link */
      .navbar a.right {
        float: right;
      }

      /* Change color on hover */
      .navbar a:hover {
        background-color: green;
        color: white;
      }

      /* Column container */
      .row {
        display: -ms-flexbox; /* IE10 */
        display: flex;
        -ms-flex-wrap: wrap; /* IE10 */
        flex-wrap: wrap;
      }

      /* Create two unequal columns that sits next to each other */
      /* Sidebar/left column */
      .side {
        -ms-flex: 30%; /* IE10 */
        flex: 30%;
        background-color: #87ceeb;
        padding: 20px;
        color: white;
      }

      /* Main column */
      .main {
        -ms-flex: 70%; /* IE10 */
        flex: 70%;
        background-color: #87ceeb;
        color: white;
        padding: 20px;
      }

      /* Fake image, just for this example */
      .fakeimg {
        background-color: #006400	;
        width: auto;
        padding: 20px;
      }

      /* Footer */
      .footer {
        padding: 20px;
        text-align: center;
        background: blue;
      }

      /* Responsive layout - when the screen is less than 700px wide, make the two columns stack on top of each other instead of next to each other */
      @media screen and (max-width: 700px) {
        .row {
          flex-direction: column;
        }
      }

      /* Responsive layout - when the screen is less than 400px wide, make the navigation links stack on top of each other instead of next to each other */
      @media screen and (max-width: 400px) {
        .navbar a {
          float: none;
          width: 100%;
        }
      }

      /* Defines Paragraph parameters */
    </style>
  </head>
  <body>
    <div class="header">
      <h1>Ballistic Geidi</h1>
      <p>Logs of all of our emotions that people feel</p>
    </div>

    <div class="row">
      <div class="side">
        <h2>List of emotions that people feel</h2>
        <h5>Depression:</h5>
        <!--         <div class="fakeimg" style="height:200px;">Beauty Salon</div> -->
        <img
          src="https://cdn.glitch.com/2388c168-d12b-4e0d-b8f8-f1c7cb599d23%2FScreen%20Shot%202021-05-15%20at%2011.18.43%20AM.png?v=1621096445405"
          style="height:200px; horizontal-align:middle"
        />
        <p>
          Depression is a common emotion through teens and adults
        </p>

        <div class="fakeimg" style="height:60px;">
         <a href="https://health.usnews.com/health-care/patient-advice/articles/activities-to-help-fight-depression">Click Here To Be Recommended Some Activities</a>
        </div>
        
        <br />
        <div class="fakeimg" style="height:60px;">
        <a href="https://www.samhsa.gov/find-help/national-helpline">Click Here To Talk To A Therapist</a>
        <br />
          
          <br />
        <div class="fakeimg" style="height:60px;">
          Click Here To Find Other People Who Experience 
        </div>
          <br />
      </div>
      <div class="main">
        <h2>Sadness</h2>
        <img
          src="https://cdn.glitch.com/2388c168-d12b-4e0d-b8f8-f1c7cb599d23%2Fsadness.jpeg?v=1621096617702"
             style="height:200px; horizontal-align:middle"
             />
                <div class="fakeimg" style="height:60px;">
          <div>
            Click Here To Be Recommended Some Activities
          </div>
        </div>
        <br />
        <div class="fakeimg" style="height:60px;">Click Here To Talk To A Therapist</div>
        <br />
        <div class="fakeimg" style="height:60px;">
          
          <a href="https://www.socialworkdegreeguide.com/30-famous-people-alive-today-battled-depression/">Click Here To Find Other People Who Experience</a>
        </div>
        
        <script
          type="text/javascript"
          src=""
        ></script>
        <script type="text/javascript">
          trends.embed.renderExploreWidget(
            "TIMESERIES",
            {
              comparisonItem: [
                { keyword: "gaming", geo: "", time: "2008-01-01 2021-04-23" }
              ],
              category: 0,
              property: "youtube"
            },
            {
              exploreQuery: "date=all_2008&gprop=youtube&q=gaming",
              guestPath: "https://trends.google.com:443/trends/embed/"
            }
          );
        </script>
        <p>
          
        </p>
        <br />
        
        
      </div>
    </div>

  </body>
</html>
