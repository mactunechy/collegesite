// variables  
const course = document.querySelector('#course-list');
const shoppingCart = document.querySelector('tbody');




// event listeners
eventListeners();

 function eventListeners(){
course.addEventListener('click',getCourse);



}



//functions


function getCourse(e){
    e.preventDefault;
    // e.preventDefault;

    if(e.target.classList.contains('add-to-cart')){
        const course = e.target.parentElement.parentElement;
        
        getCourseInfo(course);
        
        
    }
    
}



function getCourseInfo(course){
    course = {
         img : course.querySelector('img').src,
         name : course.querySelector('.card-text').textContent,
         prize : course.querySelector('h5').textContent,
         id : course.getAttribute('id')
        
        
        
    }
    
    addToCart(course);
    
    
}

function addToCart(course){
    const courseItem = document.createElement('tr');
    
    courseItem.innerHTML = `
            <tr>
                <td>
                <img src='${course.img}' class=" shopping-cart-img thumbnail">
                
                </td>
            
             <td>
               <p> ${course.name}</p>

                </td>
             <td>
              <p>  ${course.prize}</p>
                
                </td>
            
            </tr>
    
    
    
    `;
    
    
    shoppingCart.appendChild(courseItem);
    
    
}




