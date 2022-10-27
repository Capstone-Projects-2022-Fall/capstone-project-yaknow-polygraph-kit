<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="index.css" />
    <scrip src="index.js" defer></script>
    <title>yaKnow - PolyGraph Test Kit</title>
  </head>
  <body>
    <div class="topnav">
      <a class="active" href="#home">Home</a>
      <a href="#news">Tests Conducted</a>
      <a href="#contact">Members</a>
      <a href="#about">Help</a>
    </div>
    <button id="button-begin">Begin Test</button>
    <button id="button-collect">Collect Test</button>

    <form id="form">
        <input type="file" id="file" name="fileupload" /><br />
        <input type="text" id="comments" placeholder="Comments" />
        <button id="button-upload">Upload</button>
    </form>
    <div id="output"></div>
    <table style="width:100%">
      <tr>
        <th>Company</th>
        <th>Contact</th>
        <th>Country</th>
      </tr>
      <tr>
        <td>Alfreds Futterkiste</td>
        <td>Maria Anders</td>
        <td>Germany</td>
      </tr>
      <tr>
        <td>Centro comercial Moctezuma</td>
        <td>Francisco Chang</td>
        <td>Mexico</td>
      </tr>
    </table>
  </body>
</html>
