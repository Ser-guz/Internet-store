$(document).ready(function () {
  var form = $("#form_buying_product");
  console.log(form);

  function basket_updating(product_id, amount, is_delete) {
    var data = {};
    data.product_id = product_id;
    data.amount = amount;

    // Защита формы
    var csrf_token = $(
      '#form_buying_product [name="csrfmiddlewaretoken"]'
    ).val();
    data["csrfmiddlewaretoken"] = csrf_token;
    // взятие url из атрибута формы action
    var url = form.attr("action");

    if (is_delete) {
      data["is_delete"] = true;
    }
    var url = form.attr("action");
    console.log(data);

    $.ajax({
      url: url,
      type: "POST",
      data: data,
      cache: true,
      // функция success() вызывается, если успешно получен ответ с сервера
      success: function (data) {
        console.log("OK");
        console.log(data.products_total_amount);
        if (data.products_total_amount || data.products_total_amount == 0) {
          $("#basket-total-amount").text(
            "(" + data.products_total_amount + ")"
          );
          console.log(data.products);
          $(".basket-items ul").html(""); // очищение кода html внутри блока, в которой функция делает запись.
          // Проход по каждому элементу, у которого k - это индекс, v - значение
          $.each(data.products, function (k, v) {
            $(".basket-items ul").append(
              "<li>" +
              v.name +
              ", " +
              v.amount +
              " шт. по " +
              v.price_per_item +
              " руб.   " +
              '<a class="delete-item" href="" data-product_id="' +
              v.id +
              '">x</a>' +
              "</li>"
            );
          });
        }
      },
      error: function () {
        console.log("error");
      }
    });
  }

  //   Присоединение события
  form.on("submit", function (e) {
    // блокировка обновления страницы при нажатии кнопки
    e.preventDefault();
    // взятие данных из форм с id, ссылка на кот. осущ-ся через #
    var amount = $("#number").val();
    console.log(amount);
    var submit_btn = $("#submit-btn");
    // взятие данных из скрытых дата-атрибутов
    var product_id = submit_btn.data("product_id");
    var product_name = submit_btn.data("name");
    var product_price = submit_btn.data("price");
    console.log(product_id);
    console.log(product_name);
    console.log(product_price);

    basket_updating(product_id, amount, (is_delete = false));
  });

  function showingBasket() {
    $(".basket-items").removeClass("d-none");
  }

  $(".basket-container").on("click", function (e) {
    e.preventDefault();
    showingBasket();
  });
  $(".basket-container").mouseover(function (e) {
    e.preventDefault();
    showingBasket();
  });
  $(".basket-container").mouseout(function (e) {
    e.preventDefault();
    showingBasket();
  });
  // удаление записи в меню "корзина" на нав.баре, но нет удаления товаров из базы данных
  $(document).on("click", ".delete-item", function (e) {
    e.preventDefault();
    product_id = $(this).data("product_id");
    amount = 0;
    basket_updating(product_id, amount, (is_delete = true));
  });

  function calculating_basket_price() {
    var total_order_price = 0
    // Цикл each с суммированием суммы заказа по ячейкам с классом=total_product_in_basket_price
    $('.total-product-in-basket-price').each(function () {
      total_order_price += parseFloat($(this).text());
    });
    // Передача суммы заказа в ячейку таблицы с id=total_order_price
    $('#total_order_price').text(total_order_price);
    console.log(total_order_price)
  };

  // Отслеживание изменения значения в ячейке с классом="product-in-basket-amount" и вызов при изменении функции 
  $(document).on('change', ".product-in-basket-amount", function () {
    var current_amount = $(this).val(); // взятие текущего количества продуктов из значения инпута
    var current_tr = $(this).closest('tr'); // нашли ближайшую строку к инпуту
    var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2); // в найденной строке искать спан с классом=""
    var total_price = parseFloat(current_amount * current_price).toFixed(2);
    current_tr.find('.total-product-in-basket-price').text(total_price);
    calculating_basket_price();
  })

  calculating_basket_price();
});
