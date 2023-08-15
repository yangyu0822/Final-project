$(document).ready( function() {
    // Data is obtained from the rand_search.cgi script and rendered
    $.getJSON('./rand_search.cgi', function(data) {
        $.each( data, function( key, val ) {
            $('#resultsList').append('<li>'+key+': '+val+'</li>');
        });
        $('#resultsList').append('<li><a href=\'https://alphafold.ebi.ac.uk/entry/'+data['Protein ID']+'\' target=\'_blank\'>HyperLink to AlphaFold Database</a></li>');
        $('#resultsList').append('<li><a href=\'http://www.uniprot.org/uniprot/?query='+data['Symbol']+'&fil=organism%3A%22Drosophila+melanogaster+%28Fruit+fly%29+%5B7227%5D%22&sort=score\' target=\'_blank\'>HyperLink to UniProt Search</a></li>');
    });

    $('#submit').click( function() {
      var frmStr = $('#odorbase_search').serialize();

      $.ajax({
          url: './search_term.cgi',
          dataType: 'json',
          data: frmStr,
          success: function(data, textStatus, jqXHR) {
            alert(data.match_count + " matches were found.");
            $('#resultsList').empty();  // Clear previous results
            $.each( data.matches, function( i, item ) {
              $('#resultsList').append('<li>Protein ID: '+item.ProteinID+'</li>');
              $('#resultsList').append('<li>Feature Type: '+item.Feature_Type+'</li>');
              $('#resultsList').append('<li>Name: '+item.Name+'</li>');
              $('#resultsList').append('<li>Symbol: '+item.Symbol+'</li>');
              $('#resultsList').append('<li>UniProt Function: '+item.UniProt_Function+'</li>');
              $('#resultsList').append('<li>Protein Family: '+item.Protein_Family+'</li>');
              $('#resultsList').append('<li><a href=\'https://alphafold.ebi.ac.uk/entry/'+item.ProteinID+'\' target=\'_blank\'>HyperLink to AlphaFold Database</a></li>');
              $('#resultsList').append('<li><a href=\'http://www.uniprot.org/uniprot/?query='+item.Symbol+'&fil=organism%3A%22Drosophila+melanogaster+%28Fruit+fly%29+%5B7227%5D%22&sort=score\' target=\'_blank\'>HyperLink to UniProt Search</a></li>');
            });
          },
          error: function(jqXHR, textStatus, errorThrown){
              alert("Failed to perform search! textStatus: (" + textStatus + ") and errorThrown: (" + errorThrown + ")");
          }
      });
      return false;  // prevents 'normal' form submission
    });
});