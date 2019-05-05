function loadData(event, brand_id){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", `http://127.0.0.1:8000/test/${brand_id}`, true);
    xhr.onload = function(){
        if(this.status == 200){
            const response = JSON.parse(this.responseText);
            let output = '';

            for(var i = 0; i < response.length; i++){
                output += `
                <div class="item item-thumbnail" id="tabcontent">
                <a href="details/${response[i].id}" class="item-image">
                    <img src="media/${response[i].image}" alt="" />
                    
                    <div class="discount">${response[i].discount_percentage}% OFF</div>
                    
                </a>
                <div class="item-info">
                    <h4 class="item-title">
                        <a href="details/${response[i].id}">${response[i].name}</a>
                    </h4>
                    <p class="item-desc">3D Touch. 12MP photos. 4K video.</p>
                    <div class="item-price">${response[i].original_price}</div>
                    
                    <div class="item-discount-price">${response[i].discount_price}</div>
                    
                </div>
            </div>

                `;
            }
            //console.log(output);
            document.getElementById('output').innerHTML = output;
        }
    }
    xhr.send();
    event.preventDefault();
}
