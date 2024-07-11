

let allcategory;

const CaregoryFun = async (id, category) => {
  const nvbtn = document.getElementsByClassName('navbt');
  for (const el of nvbtn) {
    el.style.backgroundColor = '#dedfde';
    el.style.color = 'black';
  }

  const all_category_view = document.getElementById(category);
  all_category_view.style.backgroundColor = "#ff1f3d";
  all_category_view.style.color = "white";
  const res = await fetch(
    `https://openapi.programming-hero.com/api/videos/category/${id}`
  );
    allcategory = await res.json();
  display(allcategory);
};
const Items = document.getElementById("Items");

// convert seconds function call
const convertSecondsToHMS=(seconds)=>{
  if(seconds>=3600){
      let hours = Math.floor(seconds / 3600);
      let minutes = Math.floor((seconds % 3600) / 60);
      return `${hours}hrs ${minutes} min ago`;
  }
  else if(seconds>=60){
      let minutes = Math.floor((seconds % 3600) / 60);
      return `${minutes} min ago`;
  }
  else{
    let second=Math.floor(seconds%60);
    if(second!=0){
      return;
    }
  }
}


// display function call
const display = (info) => {
  if(info.data.length==0){
    Items.innerHTML="";
    const Drawing=document.createElement("div");
    Drawing.classList.add("Drawing_class");
    Drawing.innerHTML=`
    <img class="Empty_img" src="/PHero-Tube-main/Icon.png" alt="">
    <h1 class="Title">Oops!! Sorry, There is no content here</h1>
    `;
    Items.appendChild(Drawing);
  }
  else{
  Items.innerHTML="";
  info.data.forEach((element) => {
    const card = document.createElement("div");
    const Thambel = document.createElement("div");
    const authorInfo = document.createElement("div");
    const authorInfoPro = document.createElement("div");
    const authorInfoDetails = document.createElement("div");
    Thambel.classList.add("Thambel_box");
    authorInfo.classList.add("AuthorInfo");
    card.classList.add("box");
    let Time=convertSecondsToHMS(element.others.posted_date)
    if (Time) {
      card.innerHTML = `
    <style>
    .box {
    width: 312px;
    height: 325px;
    border-radius: 6px;
    }
  </style>
  
  `;
    Thambel.style.backgroundImage=`url(${element.thumbnail})`;
    Thambel.innerHTML = `<style>
    .Thambel_box{
      width: 312px;
    height: 200px;
    border-radius: 6px;
    background-size: cover;
    background-repeat: no-repeat;
    }
    </style>
    <div class="post_time">
  <h9 class="Time_post">${Time}</h9>
  </div>
  `;
    }

    else {
      card.innerHTML = `
    <style>
    .box {
    width: 312px;
    height: 325px;
    border-radius: 6px;
    }
  </style>
  
  `;
    Thambel.style.backgroundImage=`url(${element.thumbnail})`;
    Thambel.innerHTML = `<style>
    .Thambel_box{
      width: 312px;
    height: 200px;
    border-radius: 6px;
    background-size: cover;
    background-repeat: no-repeat;
    }
    </style>
  `;
    }
    
    card.appendChild(Thambel);
    element.authors.forEach((Author) => {
      authorInfoPro.innerHTML = `<img class="Profie_img" src=${Author.profile_picture} alt="">
      `;
      authorInfoDetails.innerHTML = `<h4>${element.title}</h4>
      <p class="VerifiedProfile">${
        Author.profile_name
      }<span id="Verified_logo">${
        Author.verified ? '<img src="/PHero-Tube-main/Group 3.png" alt="">' : ""
      }</span></p>
      <p>${element.others.views} views</p>`;
      authorInfo.appendChild(authorInfoPro);
    });
    authorInfo.appendChild(authorInfoDetails);
    card.appendChild(authorInfo);
    Items.appendChild(card);
  });
  }
};
const SortByView=()=>{
  allcategory.data.sort((a, b) => {
    const viewsA = parseFloat(a.others.views);
    const viewsB = parseFloat(b.others.views);
  
    return viewsB - viewsA;
  });
  
  display(allcategory);
  
}

CaregoryFun("1000", "All_Category");
