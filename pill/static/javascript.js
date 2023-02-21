jQuery(document).ready(function() {
  var allItems = [],
      lineFull = [],
      firstItem,
      arr2 = [],
      arr1 = [],
      count,
      count2,
      actualEl,
      lineGap,
      firstArr2,
      last,
      firstArr1;

  allItems = $('.per-carousel .item').toArray();
  firstItem = allItems[0];
  allItems.shift();
  arr1 = allItems.splice(0, Math.ceil(allItems.length /2));
  arr2 = allItems;
  lineFull = [...arr1, ...arr2];
  arr2.reverse();
  carouselClass();

  function carouselClass() {  
      $(".per-carousel .item").removeClass('center-item before-item after-item');
      $(".per-carousel .item").css('z-index','0');
      $(firstItem).addClass('center-item');
      $(firstItem).css('z-index','90');
      count = arr1.length;
      count2 = arr2.length;
      actualEl = lineFull.indexOf(firstItem);
      lineGap = (((actualEl + 2)*100)/(lineFull.length + 1));
      $(".actual-line").css('width',lineGap + '%');
      for(i = 0; i < arr1.length; i++) {
          if (arr1.length == count) {
              $(arr1[i]).addClass('second-item');
          }
          count--;
          $(arr1[i]).addClass('after-item');
          $(arr1[i]).css('z-index', count);
      }

      for(i = 0; i < arr2.length ; i++) {
          if (arr2.length == count2) {
              $(arr2[i]).addClass('last-item');
          }
          count2--;
          $(arr2[i]).addClass('before-item');
          $(arr2[i]).css('z-index', count2);
      }
  }

  function sliding(firstArray, secondArray) {
      firstArr2 = secondArray.pop();
      firstArray.push(firstArr2);
      secondArray.unshift(firstItem);
      last = secondArray[-1];
      firstArray.push(last);
      firstArr1 = firstArray[0];
      firstItem = firstArr1;
      firstArray.shift();
      firstArray.pop();
      $(".per-carousel .item").removeClass('center-item before-item after-item last-item second-item');
      carouselClass();
  }

  $(document).on('click', '.second-item, .per-next', function() {
      sliding(arr1, arr2);
  });

  $(document).on('click', '.last-item, .per-prev', function() {
      sliding(arr2, arr1);
  });

  $(".per-carousel").on("touchstart", function(event){
      console.log("work");
  var xClick = event.originalEvent.touches[0].pageX;
      $(this).one("touchmove", function(event){
          var xMove = event.originalEvent.touches[0].pageX;
          if( Math.floor(xClick - xMove) > 5 ){
              sliding(arr1, arr2);
          }
          else if( Math.floor(xClick - xMove) < -5 ){
              sliding(arr2, arr1);
          }
      });
      $(".per-carousel").on("touchend", function(){
              $(this).off("touchmove");
      });
  });
});