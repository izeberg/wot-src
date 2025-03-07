package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _2d8d6ca1bd20524ffb955b646c3e0a2f75097fb2dcc99a12e060e615f1928829_flash_display_Sprite extends Sprite
   {
       
      
      public function _2d8d6ca1bd20524ffb955b646c3e0a2f75097fb2dcc99a12e060e615f1928829_flash_display_Sprite()
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
