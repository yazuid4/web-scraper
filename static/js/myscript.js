const containerTag = document.querySelector('.my-container-tag')
const input = document.querySelector('.my-container-tag input')

tags = []


function createTag(label) {
	 const div = document.createElement('div')
	 div.setAttribute('class', 'my-tag')
	 const span  = document.createElement('span')
	 span.innerHTML = label
	 const span2 = document.createElement('span')
	 span2.setAttribute('id', 'tag-icon')
	 span2.setAttribute('class', 'material-icons')
	 span2.setAttribute('data-item', label)
	 span2.innerHTML = 'close'
	 div.appendChild(span)
	 div.appendChild(span2)

	 return div
	}


function reset(){
	 document.querySelectorAll('.my-tag').forEach(function(tag){
	 	  tag.parentElement.removeChild(tag)
	 })
}


function addTag() {
	reset()
	tags.slice().reverse().forEach(function(tag) {
		const input = createTag(tag);
		containerTag.prepend(input)
	})
}
	

input.addEventListener('keyup', function(e){
	 if(e.key == 'Enter'){
	 	 tags.push(input.value)
	 	 addTag()
	 	 input.value = ''
	 }
})


document.addEventListener('click', function(e){
	if(e.target.tagName == 'SPAN'){
		 const value = e.target.getAttribute('data-item')
		 const idx = tags.indexOf(value)
		 tags = [...tags.slice(0, idx), ...tags.slice(idx+1)]
		 addTag()
	  }
})




// Submit
$(document).ready(function(){
     $(function() {

        $("#button-addon2").click(function(e){
            
            e.preventDefault()

            $('#myform1').attr('action','/scp/');

            $('<input>').attr({
			    type: 'hidden',
			    id: 'keys',
			    name: 'mykeys',
			    value: tags
			  }).appendTo('form');

            $('#myform1').submit();	 	   
   });
  });
});
