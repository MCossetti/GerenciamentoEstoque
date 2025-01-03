$(document).ready(function () {
  //insere classe no primeiro item de produto
  $("#id_estoque-0-produto").addClass("clProduto");
  $("#id_estoque-0-quantidade").addClass("clQuantidade");

  // Desabilita o primeiro campo 'Saldo'
  $("#id_estoque-0-saldo").prop("type", "hidden");

  // Cria um span para mostrar o saldo na tela.
  $('label[for="id_estoque-0-saldo"]').append(
    '<span id="id_estoque-0-saldo-span" class="lead" style="padding-left: 10px;"></span>'
  );

  $("#add-item").click(function (ev) {
    ev.preventDefault();
    var count = $("#estoque").children().length;
    var tmplMarkup = $("#item-estoque").html();
    var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
    $("div#estoque").append(compiledTmpl);

    //update form count
    $("#id_estoque-TOTAL_FORMS").attr("value", count + 1);

    // Desabilita o campo 'Saldo'
    $("#id_estoque-" + count + "-saldo").prop("type", "hidden");

    //some animate to scroll to view our new form
    $("html, body").animate(
      {
        scrollTop: $("#add-item").position().top - 200,
      },
      800
    );

    $("#id_estoque-" + count + "-produto").addClass("clProduto");
    $("#id_estoque-" + count + "-quantidade").addClass("clQuantidade");
    // Cria um span para mostrar o saldo na tela.
    $('label[for="id_estoque-' + count + '-saldo"]').append(
      '<span id="id_estoque-' +
        count +
        '-saldo-span" class="lead" style="padding-left: 10px;"></span>'
    );
  });
});

let estoque, saldo, campo, campo2, quantidade;

$(document).on("change", ".clProduto", function () {
  let self = $(this);
  let pk = $(this).val();
  let url = "/produto/" + pk + "/json/";

  $.ajax({
    url: url,
    type: "GET",
    success: function (response) {
      estoque = response.data[0].estoque;
      campo = self.attr("id").replace("produto", "quantidade");
      // Remove o valor do campo 'quantidade'
      $("#" + campo).val("");
    },
    error: function (xhr) {},
  });
});

$(document).on("change", ".clQuantidade", function () {
  quantidade = $(this).val();

  // Aqui é feito o cálculo de soma do estoque
  saldo = Number(quantidade) + Number(estoque);
  campo = $(this).attr("id").replace("quantidade", "saldo");

  // Desabilita o 'Saldo'
  $("#" + campo).prop("type", "hidden");

  // Atribui o saldo ao campo 'saldo'
  $("#" + campo).val(saldo);
  campo2 = $(this).attr("id").replace("quantidade", "saldo-span");

  // Atrubui o saldo ao campo 'id_estoque-x-saldo-span'
  $("#" + campo2).text(saldo);
});
