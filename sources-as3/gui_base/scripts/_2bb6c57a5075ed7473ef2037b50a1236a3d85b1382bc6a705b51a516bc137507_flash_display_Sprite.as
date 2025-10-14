package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _2bb6c57a5075ed7473ef2037b50a1236a3d85b1382bc6a705b51a516bc137507_flash_display_Sprite extends Sprite
   {
       
      
      public function _2bb6c57a5075ed7473ef2037b50a1236a3d85b1382bc6a705b51a516bc137507_flash_display_Sprite()
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
