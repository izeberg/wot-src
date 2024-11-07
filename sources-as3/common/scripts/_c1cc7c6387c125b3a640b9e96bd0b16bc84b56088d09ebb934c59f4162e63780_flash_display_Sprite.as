package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _c1cc7c6387c125b3a640b9e96bd0b16bc84b56088d09ebb934c59f4162e63780_flash_display_Sprite extends Sprite
   {
       
      
      public function _c1cc7c6387c125b3a640b9e96bd0b16bc84b56088d09ebb934c59f4162e63780_flash_display_Sprite()
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
