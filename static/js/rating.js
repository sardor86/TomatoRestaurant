const stars = document.getElementsByClassName('star');
let rating_value = document.getElementById('rating');

function rating_star(data_value)
{
    rating_value.value = data_value
    for(let i = 0; i < data_value; i++)
    {
        stars[i].querySelector('span').textContent = '★';
    }
    for(let i = data_value; i < 5; i++)
    {
        stars[i].querySelector('span').textContent = '☆';
    }
}

