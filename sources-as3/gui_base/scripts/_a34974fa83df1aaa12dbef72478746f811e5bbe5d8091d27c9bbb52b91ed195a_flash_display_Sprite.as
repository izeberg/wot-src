package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a34974fa83df1aaa12dbef72478746f811e5bbe5d8091d27c9bbb52b91ed195a_flash_display_Sprite extends Sprite
   {
       
      
      public function _a34974fa83df1aaa12dbef72478746f811e5bbe5d8091d27c9bbb52b91ed195a_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
